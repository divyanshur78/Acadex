
import fs from "node:fs";
import path from "node:path";

const OWNER = "divyanshur78";
const REPO = "Acadex";
const BRANCH = "main";

const API_URL = `https://api.github.com/repos/${OWNER}/${REPO}/git/trees/${BRANCH}?recursive=1`;
const OUTPUT = path.resolve("data/resource-index.js");

function encodeGitHubPath(filePath) {
  return filePath.split("/").map(encodeURIComponent).join("/");
}

function getResourceDetails(filePath) {
  const parts = filePath.split("/");
  const relative = parts.slice(1);

  const semesterIndex = relative.findIndex(part =>
    /^Semester-\d+$/i.test(part)
  );

  if (semesterIndex === -1) return null;

  const folderParts = relative.slice(0, semesterIndex);
  const fileName = parts.at(-1);
  const semester = Number(relative[semesterIndex].match(/\d+/)[0]);

  const programme = folderParts[0] || "Other";
  let branch = "";
  let specialisation = "";

  if (programme === "BTech") {
    if (folderParts[1] === "CSE") {
      branch = "CSE";
      specialisation = folderParts[2] || "Core";
    } else {
      branch = folderParts[1] || "";
    }
  } else {
    branch = folderParts.slice(1).join(" / ");
  }

  const encodedPath = encodeGitHubPath(filePath);

  return {
    id: filePath,
    programme,
    branch,
    specialisation,
    semester,
    fileName,
    title: fileName.replace(/\.pdf$/i, ""),
    type: "PDF",
    path: filePath,
    url: `https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/${encodedPath}`,
    githubUrl: `https://github.com/${OWNER}/${REPO}/blob/${BRANCH}/${encodedPath}`
  };
}

async function main() {
  console.log("Reading Acadex resource folders...");

  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error(`GitHub API error: ${response.status}`);
  }

  const result = await response.json();

  if (!Array.isArray(result.tree) || result.truncated) {
    throw new Error("GitHub tree is invalid or truncated.");
  }

  const resources = result.tree
    .filter(item =>
      item.type === "blob" &&
      item.path.startsWith("Acadex_Resources/") &&
      /\.pdf$/i.test(item.path)
    )
    .map(item => getResourceDetails(item.path))
    .filter(Boolean)
    .sort((a, b) => a.path.localeCompare(b.path));

  const database = {
    repository: `${OWNER}/${REPO}`,
    branch: BRANCH,
    generatedAt: new Date().toISOString(),
    totalResources: resources.length,
    resources
  };

  fs.mkdirSync(path.dirname(OUTPUT), { recursive: true });

  fs.writeFileSync(
    OUTPUT,
    "// Automatically generated. Do not edit manually.\n" +
    "window.ACADEX_RESOURCES = " +
    JSON.stringify(database, null, 2) + ";\n",
    "utf8"
  );

  console.log(`Done! ${resources.length} PDF files indexed.`);
  console.log(`Created: ${OUTPUT}`);
}

main().catch(error => {
  console.error("Resource generation failed:", error);
  process.exitCode = 1;
});

