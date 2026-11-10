(function () {
"use strict";

const container=document.getElementById("availableSemesterPdfs");
const page=document.querySelector(".semester-page-main");
if(!container || !page) return;

const resources=window.ACADEX_RESOURCES?.resources;
if(!Array.isArray(resources)){
 container.textContent="Resource database could not be loaded.";
 return;
}

const selected=resources.filter(r =>
 r.programme===page.dataset.programme &&
 r.branch===page.dataset.branch &&
 r.specialisation==="AI-ML" &&
 Number(r.semester)===Number(page.dataset.semesterNumber)
);

container.replaceChildren();

selected.forEach(resource=>{
 const fileUrl=resource.path.split("/").map(encodeURIComponent).join("/");
 const actualUrl="https://media.githubusercontent.com/media/divyanshur78/Acadex/main/"+fileUrl;

 const card=document.createElement("article");
 card.className="semester-resource-card";

 const title=document.createElement("h3");
 title.textContent=resource.fileName;

 const view=document.createElement("a");
 view.href="../../pdf-viewer.html?file="+encodeURIComponent(actualUrl);
 view.textContent="View PDF";

 const download=document.createElement("a");
 download.href=actualUrl;
 download.download=resource.fileName;
 download.textContent="Download";

 card.append(title,view,download);
 container.appendChild(card);
});

console.log("Acadex PDFs loaded:",selected.length);
})();

