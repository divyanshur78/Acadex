(function () {
  "use strict";

  const container = document.getElementById("availableSemesterPdfs");
  const countEl = document.getElementById("semesterPdfCount");
  const page = document.querySelector(".semester-page-main");
  if (!container || !page) return;

  const resources = window.ACADEX_RESOURCES?.resources;
  if (!Array.isArray(resources)) {
    container.textContent = "Resource database could not be loaded.";
    return;
  }

  const prog = page.dataset.programme || "";
  const branch = page.dataset.branch || "";
  const specSlug = page.dataset.specialisationId || "";
  const semNum = Number(page.dataset.semesterNumber);

  // Mapping from slug to resource index values
  const specMap = {
    "artificial-intelligence-machine-learning": "AI-ML",
    "data-science-analytics": "Data-Science",
    "cyber-security": "Cybersecurity",
    "software-engineering": "Software-Engineering",
    "cloud-computing": "Cloud-Computing",
    "internet-of-things": "IoT"
  };

  const branchMap = {
    "civil-engineering": "Civil",
    "mechanical-engineering": "Mechanical",
    "electrical-engineering": "Electrical"
  };

  const selected = resources.filter(r => {
    if (Number(r.semester) !== semNum) return false;

    // CS & IT specialisations
    if (prog === "BTech" && branch === "CSE") {
      const targetSpec = specMap[specSlug] || "Core";
      return r.programme === "BTech" && r.branch === "CSE" && r.specialisation === targetSpec;
    }

    // Engineering branches
    if (prog === "BTech") {
      const targetBranch = branchMap[specSlug] || branch;
      return r.programme === "BTech" && r.branch.toLowerCase() === targetBranch.toLowerCase();
    }

    // Agriculture
    if (prog === "Agriculture" || page.dataset.academicField === "agriculture") {
      return r.programme === "Agriculture";
    }

    // Law
    if (prog === "Law" || page.dataset.academicField === "law") {
      return r.programme === "Law";
    }

    // Pharmacy
    if (prog === "Pharmacy" || page.dataset.academicField === "pharmaceutical-sciences") {
      return r.programme === "Pharmacy";
    }

    // Management
    if (prog === "Management" || page.dataset.academicField === "management-commerce") {
      return r.programme === "Management";
    }

    return false;
  });

  container.replaceChildren();

  if (countEl) {
    countEl.textContent = `${selected.length} verified PDF ${selected.length === 1 ? 'resource' : 'resources'} available for this semester.`;
  }

  if (selected.length === 0) {
    const empty = document.createElement("p");
    empty.className = "semester-pending";
    empty.style.gridColumn = "1/-1";
    empty.textContent = "No indexed PDFs are currently mapped to this selection. Study material will appear here once verified.";
    container.appendChild(empty);
    return;
  }

  selected.forEach(resource => {
    const fileUrl = resource.path.split("/").map(encodeURIComponent).join("/");
    const actualUrl = "https://media.githubusercontent.com/media/divyanshur78/Acadex/main/" + fileUrl;

    const card = document.createElement("article");
    card.className = "semester-resource-card";

    const title = document.createElement("h3");
    let displayTitle = resource.title || resource.fileName.replace(/\.pdf$/i, "");
    displayTitle = displayTitle.replace(/[-_]/g, " ").replace(/\b\w/g, l => l.toUpperCase());
    title.textContent = displayTitle;

    const actions = document.createElement("div");
    actions.style.display = "flex";
    actions.style.gap = "10px";
    actions.style.marginTop = "12px";

    const view = document.createElement("a");
    view.href = "../../pdf-viewer.html?file=" + encodeURIComponent(actualUrl);
    view.textContent = "View PDF";
    view.target = "_blank";
    view.rel = "noopener noreferrer";
    view.className = "track-primary-button";
    view.style.padding = "6px 14px";
    view.style.fontSize = "12px";

    const download = document.createElement("a");
    download.href = actualUrl;
    download.download = resource.fileName;
    download.textContent = "Download";
    download.target = "_blank";
    download.rel = "noopener noreferrer";
    download.className = "track-secondary-button";
    download.style.padding = "6px 14px";
    download.style.fontSize = "12px";

    actions.append(view, download);
    card.append(title, actions);
    container.appendChild(card);
  });

  console.log("Acadex Semester PDFs loaded:", selected.length);
})();
