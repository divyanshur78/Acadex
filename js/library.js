
(() => {
  "use strict";

  // Load the generated academic resource database
  const database = window.ACADEX_RESOURCES;

  const searchInput = document.getElementById("resource-search");
  const programmeSelect = document.getElementById("resource-programme");
  const branchSelect = document.getElementById("resource-branch");
  const semesterSelect = document.getElementById("resource-semester");
  const resultsContainer = document.getElementById("resource-results");
  const countElement = document.getElementById("resource-count");

  // Stop if this page does not contain the resource browser
  if (!resultsContainer) return;

  // Check whether the resource database loaded successfully
  if (!database || !Array.isArray(database.resources)) {
    resultsContainer.textContent =
      "Resource database could not be loaded. Please try again.";

    if (countElement) {
      countElement.textContent = "Resources unavailable";
    }

    console.error("Acadex resource database is missing.");
    return;
  }

  const resources = database.resources;

  // Get unique, alphabetically sorted values
  function uniqueSorted(values) {
    return [...new Set(values.filter(Boolean))]
      .sort((a, b) => a.localeCompare(b));
  }

  // Add options to a dropdown
  function addOptions(select, values, placeholder) {
    select.replaceChildren();

    const firstOption = document.createElement("option");
    firstOption.value = "";
    firstOption.textContent = placeholder;
    select.appendChild(firstOption);

    values.forEach(value => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      select.appendChild(option);
    });
  }

  // Build a readable branch/specialisation label
  function getBranchLabel(resource) {
    return [
      resource.branch,
      resource.specialisation
    ].filter(Boolean).join(" / ");
  }

  // Update branch options according to selected programme
  function updateBranches() {
    const selectedProgramme = programmeSelect.value;

    const matchingResources = resources.filter(resource =>
      !selectedProgramme ||
      resource.programme === selectedProgramme
    );

    addOptions(
      branchSelect,
      uniqueSorted(matchingResources.map(getBranchLabel)),
      "All branches"
    );
  }

  // Update semester options according to programme and branch
  function updateSemesterOptions() {
    const selectedProgramme = programmeSelect.value;
    const selectedBranch = branchSelect.value;

    const matchingResources = resources.filter(resource => {
      const matchesProgramme =
        !selectedProgramme ||
        resource.programme === selectedProgramme;

      const matchesBranch =
        !selectedBranch ||
        getBranchLabel(resource) === selectedBranch;

      return matchesProgramme && matchesBranch;
    });

    const semesters = [
      ...new Set(matchingResources.map(resource => resource.semester))
    ].sort((a, b) => a - b);

    addOptions(
      semesterSelect,
      semesters.map(String),
      "All semesters"
    );
  }

  // Create an individual PDF resource card
  function createResourceCard(resource) {
    const card = document.createElement("article");
    card.className = "resource-result-card";

    const title = document.createElement("h3");
    title.textContent = resource.fileName;

    const meta = document.createElement("p");
    meta.className = "resource-result-meta";
    meta.textContent = [
      resource.programme,
      getBranchLabel(resource),
      `Semester ${resource.semester}`
    ].filter(Boolean).join(" â€¢ ");

    const actions = document.createElement("div");
    actions.className = "resource-actions";

    // Build actual GitHub LFS PDF URL
    const pdfUrl = "https://media.githubusercontent.com/media/divyanshur78/Acadex/main/" +
      resource.path.split("/").map(encodeURIComponent).join("/");

    // View PDF
    const viewLink = document.createElement("a");
    viewLink.href = "pdf-viewer.html?file=" + encodeURIComponent(pdfUrl);
    viewLink.target = "_blank";
    viewLink.rel = "noopener noreferrer";
    viewLink.textContent = "View PDF";

    // Download PDF
    const downloadLink = document.createElement("a");
    downloadLink.href = pdfUrl;
    downloadLink.target = "_blank";
    downloadLink.rel = "noopener noreferrer";
    downloadLink.download = resource.fileName;
    downloadLink.className = "secondary";
    downloadLink.textContent = "Download";

    actions.append(viewLink, downloadLink);
    card.append(title, meta, actions);

    return card;
  }

  // Apply search and filters, then display matching resources
  function renderResources() {
    const query = searchInput.value.trim().toLowerCase();
    const selectedProgramme = programmeSelect.value;
    const selectedBranch = branchSelect.value;
    const selectedSemester = semesterSelect.value;

    const filteredResources = resources.filter(resource => {
      const searchableText = [
      resource.fileName,
      resource.title,
      resource.programme,
      resource.branch,
      resource.specialisation,
      resource.path,
      `semester ${resource.semester}`
].filter(Boolean).join(" ").toLowerCase();

      const matchesSearch =
        !query || searchableText.includes(query);

      const matchesProgramme =
        !selectedProgramme ||
        resource.programme === selectedProgramme;

      const matchesBranch =
        !selectedBranch ||
        getBranchLabel(resource) === selectedBranch;

      const matchesSemester =
        !selectedSemester ||
        resource.semester === Number(selectedSemester);

      return (
        matchesSearch &&
        matchesProgramme &&
        matchesBranch &&
        matchesSemester
      );
    });

    resultsContainer.replaceChildren();

    if (countElement) {
      countElement.textContent =
        `${filteredResources.length} of ${resources.length} PDFs`;
    }

    if (filteredResources.length === 0) {
      const emptyMessage = document.createElement("p");
      emptyMessage.className = "resource-empty";
      emptyMessage.textContent =
        "No resources found. Try changing your search or filters.";

      resultsContainer.appendChild(emptyMessage);
      return;
    }

    const fragment = document.createDocumentFragment();

    filteredResources.forEach(resource => {
      fragment.appendChild(createResourceCard(resource));
    });

    resultsContainer.appendChild(fragment);
  }

  // Initialise programme dropdown
  addOptions(
    programmeSelect,
    uniqueSorted(resources.map(resource => resource.programme)),
    "All programmes"
  );

  // Initialise dependent dropdowns and display resources
  updateBranches();
  updateSemesterOptions();
  renderResources();

  // Search event
  searchInput.addEventListener("input", renderResources);

  // Programme filter event
  programmeSelect.addEventListener("change", () => {
    updateBranches();
    updateSemesterOptions();
    renderResources();
  });

  // Branch filter event
  branchSelect.addEventListener("change", () => {
    updateSemesterOptions();
    renderResources();
  });

  // Semester filter event
  semesterSelect.addEventListener("change", renderResources);

  console.log(
    `Acadex Library loaded successfully: ${resources.length} PDFs`
  );

})();


