/*
 ACADEX - ACADEMIC RESOURCE DATABASE

Programmes:
1. Agriculture
2. Pharmacy
3. Law
4. Management - BBA
5. Management - MBA
6. BTech - 10 branches/specialisations
*/

export const academicResources = {
  fields: [
    { id: "field-agriculture", name: "Agriculture" },
    { id: "field-pharmacy", name: "Pharmacy" },
    { id: "field-law", name: "Law" },
    { id: "field-management", name: "Management" },
    { id: "field-engineering", name: "Engineering" }
  ],

  programmes: [
    { id: "agriculture", fieldId: "field-agriculture", name: "B.Sc. Agriculture" },
    { id: "pharmacy", fieldId: "field-pharmacy", name: "B.Pharm" },
    { id: "law", fieldId: "field-law", name: "BA LL.B." },
    { id: "bba", fieldId: "field-management", name: "BBA" },
    { id: "mba", fieldId: "field-management", name: "MBA" },

    { id: "btech-cse-ai-ml", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Artificial Intelligence and Machine Learning" },
    { id: "btech-cse-cloud", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Cloud Computing" },
    { id: "btech-cse-core", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Core" },
    { id: "btech-cse-cybersecurity", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Cybersecurity" },
    { id: "btech-cse-data-science", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Data Science" },
    { id: "btech-cse-iot", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Internet of Things" },
    { id: "btech-cse-software-engineering", fieldId: "field-engineering", name: "B.Tech CSE ΓÇô Software Engineering" },
    { id: "btech-civil", fieldId: "field-engineering", name: "B.Tech Civil Engineering" },
    { id: "btech-electrical", fieldId: "field-engineering", name: "B.Tech Electrical Engineering" },
    { id: "btech-mechanical", fieldId: "field-engineering", name: "B.Tech Mechanical Engineering" }
  ],

  semesters: [],
  subjects: [],
  resources: []
};

// PROGRAMME FOLDER MAPPING

const programmeFolders = {
  agriculture: "Agriculture",
  pharmacy: "Pharmacy",
  law: "Law",
  bba: "Management/bba",
  mba: "Management/mba",

  "btech-cse-ai-ml": "BTech/CSE/AI-ML",
  "btech-cse-cloud": "BTech/CSE/Cloud-Computing",
  "btech-cse-core": "BTech/CSE/Core",
  "btech-cse-cybersecurity": "BTech/CSE/Cybersecurity",
  "btech-cse-data-science": "BTech/CSE/Data-Science",
  "btech-cse-iot": "BTech/CSE/IoT",
  "btech-cse-software-engineering": "BTech/CSE/Software-Engineering",
  "btech-civil": "BTech/Civil",
  "btech-electrical": "BTech/Electrical",
  "btech-mechanical": "BTech/Mechanical"
};

// SEMESTER COUNTS

const semesterCounts = {
  agriculture: 6,
  pharmacy: 8,
  law: 10,
  bba: 6,
  mba: 4,

  "btech-cse-ai-ml": 8,
  "btech-cse-cloud": 8,
  "btech-cse-core": 8,
  "btech-cse-cybersecurity": 8,
  "btech-cse-data-science": 8,
  "btech-cse-iot": 8,
  "btech-cse-software-engineering": 8,
  "btech-civil": 8,
  "btech-electrical": 8,
  "btech-mechanical": 8
};

// GENERATE SEMESTER RECORDS

Object.entries(semesterCounts).forEach(([programmeId, count]) => {
  for (let i = 1; i <= count; i++) {
    academicResources.semesters.push({
      id: `${programmeId}-semester-${i}`,
      programmeId,
      name: `Semester ${i}`,
      number: i
    });
  }
});

// RESOURCE BUILDER

function addSemesterResources(programmeId, semesterNumber, files) {
  const semesterId = `${programmeId}-semester-${semesterNumber}`;
  const folder = programmeFolders[programmeId];

  files.forEach(([title, fileName], index) => {
    const fileUrl = fileName
      ? `Acadex_Resources/${folder}/Semester-${semesterNumber}/${fileName}`
      : null;

    academicResources.resources.push({
      id: `res-${programmeId}-s${semesterNumber}-${String(index + 1).padStart(3, "0")}`,
      title,
      type: "pdf",
      programmeId,
      semesterId,
      subjectId: null,
      fileUrl
    });
  });
}

// AGRICULTURE

addSemesterResources("agriculture", 1, [
  ["Soil Science", "soil_science.pdf"],
  ["Agronomy", "agronomy.pdf"],
  ["Communication Skills", "communication_skills.pdf"]
]);

addSemesterResources("agriculture", 2, [
  ["Entrepreneurship Development and Business Communication", "entrepreneurship.pdf"],
  ["Fundamentals of Plant Pathology", "plant_pathology.pdf"],
  ["Introduction to Nematology", "nematology.pdf"]
]);

addSemesterResources("agriculture", 3, [
  ["Introduction to Nematology", null],
  ["Principles of Genetics", null],
  ["Entrepreneurship Development and Business Communication", null],
  ["Fundamentals of Extension Education", null]
]);

addSemesterResources("agriculture", 4, [
  ["B.Sc. Agriculture Lab Manual ΓÇô 4th Semester", null],
  ["Problematic Soils and Their Management", null],
  ["Water Management Handbook", null],
  ["Artificial Intelligence in Agriculture", null],
  ["Farm Power and Machinery", null]
]);

addSemesterResources("agriculture", 5, [
  ["B.Sc. Agriculture Lab Manual ΓÇô Crop Production Technology-I (Kharif Crops)", null],
  ["Practical Manual ΓÇô Pests of Crops and Stored Grain and Their Management", null],
  ["Weed Management (ICAR Syllabus)", null],
  ["Agricultural Marketing, Trade and Prices", null],
  ["Textbook of Agricultural Meteorology", null]
]);

addSemesterResources("agriculture", 6, [
  ["Renewable Energy in Agriculture", null],
  ["Seed Science and Technology: Biology, Production, Quality", null],
  ["Essentials of Statistics in Agricultural Sciences", null],
  ["Biotechnology Fundamentals ΓÇô 3rd Edition", null],
  ["Practical Manual on Crop Improvement II (Rabi Crops)", null]
]);

// PHARMACY

addSemesterResources("pharmacy", 1, [
  ["Introduction of Pharmacognosy", "Introduction of pharmacognosy.pdf"],
  ["Textbook of Pharmaceutics-I", "Textbook+of+Pharmaceutics-I.pdf"],
  ["Anatomy, Physiology and Pathophysiology", "ANATOMY-PHYSIOLOGY-AND-PATHOPHYSIOLOGY_PHARMACY.pdf"]
]);

addSemesterResources("pharmacy", 2, [
  ["Textbook of Biochemistry for Medical Students ΓÇô D. M. Vasudevan", null],
  ["Introductory Biostatistics ΓÇô Chap T. Le", null],
  ["Pharmaceutical Organic Chemistry ΓÇô Dr. V. Alagarsamy", null]
]);

addSemesterResources("pharmacy", 3, [
  ["Pharmaceutical Engineering", null],
  ["Pharmaceutical Microbiology ΓÇô Tim Sandle", null],
  ["Environmental Science (AECC)", null],
  ["A Textbook on Heterocyclic Compounds ΓÇô Mahesh B. Swami", null],
  ["Human Values and Professional Ethics ΓÇô R. R. Gaur et al.", null]
]);

addSemesterResources("pharmacy", 4, [
  ["Basic & Clinical Pharmacology ΓÇô 14th Edition", null],
  ["Textbook of Herbal Drug Technology", null]
]);

addSemesterResources("pharmacy", 5, [
  ["Textbook of Industrial Pharmacognosy ΓÇô A. N. Kalia", null],
  ["Textbook of Biochemistry for Medical Students ΓÇô 6th Edition", null],
  ["Innovation, Startups and Entrepreneurship ΓÇô MRCET Lecture Notes", null]
]);

addSemesterResources("pharmacy", 6, [
  ["Pharmaceutical Jurisprudence and Regulatory Affairs", null],
  ["Advanced Pharmacognosy and Pharmacobiotechnology ΓÇô Ashutosh Kar", null],
  ["Role of Artificial Intelligence in Pharmaceutical Sciences", null]
]);

addSemesterResources("pharmacy", 7, [
  ["cosmeceuticals-and-active-cosmetics", "cosmeceuticals-and-active-cosmetics.pdf"],
  ["MORDERN-ANALYTICAL-TECHNIQUES(1)", "MORDERN-ANALYTICAL-TECHNIQUES(1).pdf"],
  ["pharmacovigilance(1)", "pharmacovigilance(1).pdf"],
  ["AI-in-Health-Care", "AI-in-Health-Care.pdf"],
  ["basic_biostatistics_and_research_methodology", "basic_biostatistics_and_research_methodology.pdf"],
  ["BioPharmaceutics_and_pharmacokinetics", "BioPharmaceutics_and_pharmacokinetics.pdf"],
  ["pharmaceutical_dosage_forms", "pharmaceutical_dosage_forms.pdf"],
  ["pharmaceutical_drug_analysic", "pharmaceutical_drug_analysic.pdf"]
]);

addSemesterResources("pharmacy", 8, [
  ["Ethical-Considerations", "Ethical-Considerations.pdf"],
  ["pharmaceuticals_productions_facilities", "pharmaceuticals_productions_facilities.pdf"],
  ["pharmacy_managements", "pharmacy_managements.pdf"],
  ["Clinical Pharmacology and Therapeutics", "Clinical Pharmacology and Therapeutics.pdf"],
  ["contolled_deug_delivery_systems", "contolled_deug_delivery_systems.pdf"]
]);

// LAW - BA LL.B.

addSemesterResources("law", 1, [
  ["General English Part-I", "General English Part-I.pdf"],
  ["INDIAN_LEGAL_HISTORY", "INDIAN_LEGAL_HISTORY.pdf"],
  ["Introduction to Economics_5", "Introduction to Economics_5.pdf"],
  ["Introduction to Sociology", "Introduction to Sociology.pdf"],
  ["law-of-torts", "law-of-torts.pdf"],
  ["political science-1", "political science-1.pdf"]
]);

addSemesterResources("law", 2, [
  ["Constitutional-LawI", "Constitutional-LawI.pdf"],
  ["CONTRACT_law", "CONTRACT_law.pdf"],
  ["english)for_law", "english)for_law.pdf"],
  ["INDIAN_LEGAL_HISTORY", "INDIAN_LEGAL_HISTORY.pdf"],
  ["Political Science-II", "Political Science-II.pdf"]
]);

addSemesterResources("law", 3, [
  ["a_constitutional_history_of_india", "a_constitutional_history_of_india.pdf"],
  ["Constitutional_law-II", "Constitutional_law-II.pdf"],
  ["family_law", "family_law.pdf"],
  ["Law of Crimes-I BNS 2024", "Law of Crimes-I BNS 2024.pdf"],
  ["law_of_contract_II", "law_of_contract_II.pdf"]
]);

addSemesterResources("law", 4, [
  ["ADMINISTRATIVE_LAW_FF", "ADMINISTRATIVE_LAW_FF.pdf"],
  ["Criminal Law II", "Criminal Law II.pdf"],
  ["law_of_property", "law_of_property.pdf"],
  ["Legal-Language-and-Legal-Reasoning2", "Legal-Language-and-Legal-Reasoning2.pdf"],
  ["Muslim Law(Family Law)", "Muslim Law(Family Law).pdf"]
]);

addSemesterResources("law", 5, [
  ["code_of_civil_procedure", "code_of_civil_procedure.pdf"],
  ["COMPANY_LAW", "COMPANY_LAW.pdf"],
  ["enviromental_law", "enviromental_law.pdf"],
  ["JURISPRUDENCE_Legal_Theory_", "JURISPRUDENCE_Legal_Theory_.pdf"],
  ["law-of-evidence-", "law-of-evidence-.pdf"]
]);

addSemesterResources("law", 6, [
  ["dispute_resolution", "dispute_resolution.pdf"],
  ["INCOME_TAX_LAW_AND_PRACTICE", "INCOME_TAX_LAW_AND_PRACTICE.pdf"],
  ["industrial_relation_and_labour_laws", "industrial_relation_and_labour_laws.pdf"],
  ["intellectual_property_rights", "intellectual_property_rights.pdf"],
  ["international_law", "international_law.pdf"]
]);

addSemesterResources("law", 7, [
  ["advance_labour_laws", "advance_labour_laws.pdf"],
  ["BANKING AND INSURANCE", "BANKING AND INSURANCE.pdf"],
  ["Company Law", "Company Law.pdf"],
  ["consumer laws", "consumer laws.pdf"],
  ["human_rights", "human_rights.pdf"],
  ["introduction-to-competition-law-", "introduction-to-competition-law-.pdf"]
]);

addSemesterResources("law", 8, [
  ["3.BAR AND BENCH RELATIONSHIP", "3.BAR AND BENCH RELATIONSHIP.pdf"],
  ["alternative-dispute-resolution", "alternative-dispute-resolution.pdf"],
  ["Cyber_laws", "Cyber_laws.pdf"],
  ["Drafting-Pleadings-and-Conveyancing", "Drafting-Pleadings-and-Conveyancing.pdf"],
  ["Interpretation of Statutes", "Interpretation of Statutes.pdf"],
  ["moot_court,mock_trial", "moot_court,mock_trial.pdf"]
]);

addSemesterResources("law", 9, [
  ["Criminology", "Criminology.pdf"],
  ["international_trade_law", "international_trade_law.pdf"],
  ["Interpretation of Statutes", "Interpretation of Statutes.pdf"],
  ["Principles-of-Land-Law", "Principles-of-Land-Law.pdf"],
  ["property_law", "property_law.pdf"],
  ["WomensAndChildrensRights", "WomensAndChildrensRights.pdf"]
]);

addSemesterResources("law", 10, [
  ["bharat_nyaya_sanhita", "bharat_nyaya_sanhita.pdf"],
  ["Legal-Aid-Handbook", "Legal-Aid-Handbook.pdf"],
  ["public_interest_litigation", "public_interest_litigation.pdf"]
]);

// MANAGEMENT - BBA

addSemesterResources("bba", 1, [
  ["Business commission", "Business commission.pdf"],
  ["Business Statistics and Business Mathematics", "Business Statistics and Business Mathematics.pdf"],
  ["BUSINESS_ECONOMICS", "BUSINESS_ECONOMICS.pdf"],
  ["Financial Accounting - BMS", "Financial Accounting - BMS.pdf"],
  ["principles_of_management", "principles_of_management.pdf"]
]);

addSemesterResources("bba", 2, [
  ["business_law", "business_law.pdf"],
  ["business_statstics", "business_statstics.pdf"],
  ["computer_application_in_business", "computer_application_in_business.pdf"],
  ["Financial Accounting II", "Financial Accounting II.pdf"],
  ["macro_economics", "macro_economics.pdf"],
  ["marketing-management", "marketing-management.pdf"]
]);

addSemesterResources("bba", 3, [
  ["Business Environment", "Business Environment.pdf"],
  ["Corporate Accounting", "Corporate Accounting.pdf"],
  ["hr_management", "hr_management.pdf"],
  ["management_information_system", "management_information_system.pdf"],
  ["organisational_behaviour", "organisational_behaviour.pdf"],
  ["Principles of Taxation Law", "Principles of Taxation Law.pdf"]
]);

addSemesterResources("bba", 4, [
  ["BUSINESS_ETHICS", "BUSINESS_ETHICS.pdf"],
  ["FINANCIAL MANAGEMENT", "FINANCIAL MANAGEMENT.pdf"],
  ["management_information_system", "management_information_system.pdf"],
  ["MARKETING_MANAGEMENT", "MARKETING_MANAGEMENT.pdf"],
  ["Production and Operations Management", "Production and Operations Management.pdf"]
]);

addSemesterResources("bba", 5, [
  ["CONSUMER_BEHAVIOUR", "CONSUMER_BEHAVIOUR.pdf"],
  ["Entrepreneur_development", "Entrepreneur_development.pdf"],
  ["INTERNATIONAL_BUSINESS", "INTERNATIONAL_BUSINESS.pdf"],
  ["Investment_Management", "Investment_Management.pdf"],
  ["LOGISTICS_AND_SUPPLY_CHAIN", "LOGISTICS_AND_SUPPLY_CHAIN.pdf"],
  ["strategic_management", "strategic_management.pdf"]
]);

addSemesterResources("bba", 6, [
  ["business_policy_and_strategic", "business_policy_and_strategic.pdf"],
  ["Entrepreneurship-Development", "Entrepreneurship-Development.pdf"],
  ["enviromental_science", "enviromental_science.pdf"],
  ["international_business_management", "international_business_management.pdf"],
  ["STRATEGIC_MANAGEMENT", "STRATEGIC_MANAGEMENT.pdf"]
]);

// MANAGEMENT - MBA

addSemesterResources("mba", 1, [
  ["Accounting for Management for MBA", "Accounting for Management for MBA.pdf"],
  ["BUSINESS_ENVIRONMENT", "BUSINESS_ENVIRONMENT.pdf"],
  ["Business_ethics_and_ethos", "Business_ethics_and_ethos.pdf"],
  ["Managerial Economics", "Managerial Economics.pdf"],
  ["organisational_behaviour", "organisational_behaviour.pdf"]
]);

addSemesterResources("mba", 2, [
  ["business_law", "business_law.pdf"],
  ["business_research_method", "business_research_method.pdf"],
  ["COST_AND_MANAGEMENT_ACCOUNTING", "COST_AND_MANAGEMENT_ACCOUNTING.pdf"],
  ["FINANCIAL MANAGEMENT", "FINANCIAL MANAGEMENT.pdf"],
  ["he_management", "he_management.pdf"],
  ["INTERNATIONAL_BUSINESS", "INTERNATIONAL_BUSINESS.pdf"],
  ["marketing-management", "marketing-management.pdf"],
  ["PRODUCTION_AND_OPERATIONS_MANAGEMENT", "PRODUCTION_AND_OPERATIONS_MANAGEMENT.pdf"]
]);

addSemesterResources("mba", 3, [
  ["business_analytics", "business_analytics.pdf"],
  ["corporate_finance", "corporate_finance.pdf"],
  ["Fundamentals of Risk Management", "Fundamentals of Risk Management.pdf"],
  ["marketing_group", "marketing_group.pdf"],
  ["PROJECT_MANAGEMENT", "PROJECT_MANAGEMENT.pdf"],
  ["strategic_management", "strategic_management.pdf"]
]);

addSemesterResources("mba", 4, [
  ["Business Ethics and Corporate Governance", "Business Ethics and Corporate Governance.pdf"],
  ["FINANCIAL_RISK_MANAGEMENT", "FINANCIAL_RISK_MANAGEMENT.pdf"],
  ["INTERNATIONAL_BUSINESS", "INTERNATIONAL_BUSINESS.pdf"],
  ["strategic_leadership", "strategic_leadership.pdf"],
  ["Management of Technology", "Management of Technology.pdf"]
]);

// BTECH - CSE AI/ML

addSemesterResources("btech-cse-ai-ml", 1, [
  ["Calculus 1", "calculus-1.pdf"],
  ["ECE", "ece.pdf"],
  ["Physics 1", "Physics-1.pdf"],
  ["Think Python", "thinkpython.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 2, [
  ["Calculus 2", "calculus-2.pdf"],
  ["Data Structures", "Data_Structures.pdf"],
  ["Discrete Mathematics", "discrete_mathematics.pdf"],
  ["DSA", "DSA.pdf"],
  ["Think Java", "thinkjava.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 3, [
  ["Computer Organization", "Computer Organization.pdf"],
  ["Discrete Math", "discrete_math.pdf"],
  ["DSA", "dsa.pdf"],
  ["Linear Algebra and Probability", "linear_algebra_and_probability.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 4, [
  ["Computer Networks", "computer-networks.pdf"],
  ["Database Design", "Database-Design.pdf"],
  ["Linear Algebra", "linear_algebra.pdf"],
  ["Operating Systems", "operating_systems.pdf"],
  ["Statistics", "stastistics.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 5, [
  ["Artificial Intelligence", "ai.pdf"],
  ["Algorithms", "Algorithms.pdf"],
  ["Computer Network and Security", "compute network and seccurity.pdf"],
  ["Statistical Learning", "stastistical_learning.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 6, [
  ["Deep Learning", "deep_learning.pdf"],
  ["Mining of Dataset", "mining_of_dataset.pdf"],
  ["Natural Language Processing", "Natural Language Processing.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 7, [
  ["Cloud Computing", "Cloud Computing.pdf"],
  ["Distributed Systems", "distributed-systems.pdf"],
  ["Information Security", "information securoty.pdf"],
  ["Reinforcement Learning", "reinforcement_learning.pdf"]
]);

addSemesterResources("btech-cse-ai-ml", 8, [
  ["Artificial Intelligence", "ai.pdf"],
  ["Machine Learning Systems Vol 1", "Machine-Learning-Systems-Vol1.pdf"],
  ["Machine Learning Systems Vol 2", "Machine-Learning-Systems-Vol2.pdf"],
  ["Research Methodology", "Research-Methodology.pdf"]
]);

// BTECH - CSE CLOUD COMPUTING

addSemesterResources("btech-cse-cloud", 1, [
  ["Basic Electrical Engineering", "Basic Electrical Engineering.pdf"],
  ["Engineering Physics", "Engineering_Physics.pdf"],
  ["Fundamentals of Computers", "Fundamentals of Computers.pdf"],
  ["Mathematics", "mathematics.pdf"]
]);

addSemesterResources("btech-cse-cloud", 2, [
  ["Computer System Architecture", "Computer System Architecture-Morris Mano third edition.pdf"],
  ["DSA", "Dsa.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Linux", "linuxfun.pdf"]
]);

addSemesterResources("btech-cse-cloud", 3, [
  ["Computer Organization and Architecture", "Computer-Organization-Architecture.pdf"],
  ["Managing Database", "MANAGING_DATABASE.pdf"],
  ["Object Oriented Analysis and Design", "Object.Oriented.Analysis.and.Design..pdf"],
  ["Operating System Concepts", "Operating-System-Concepts.pdf"]
]);

addSemesterResources("btech-cse-cloud", 4, [
  ["Distributed System", "distributed_system.pdf"],
  ["Network Security", "network_security.pdf"],
  ["Virtualization", "virtualization.pdf"],
  ["Web Application", "WebApplication.pdf"]
]);

addSemesterResources("btech-cse-cloud", 5, [
  ["Cloud Computing", "CLOUD COMPUTING.pdf"],
  ["Cloud Infrastructure Services", "cloudinfrastructure_services.pdf"],
  ["Distributed Computing", "distributed_computing.pdf"]
]);

addSemesterResources("btech-cse-cloud", 6, [
  ["Cloud Databases", "Cloud Databases.pdf"],
  ["Cloud Computing", "cloud_computing.pdf"],
  ["Cloud Security", "cloud_security.pdf"],
  ["Containerization", "containerization.pdf"]
]);

addSemesterResources("btech-cse-cloud", 7, [
  ["Cloud Technologies", "cloud_technologies.pdf"],
  ["Modern DevOps", "Mordern-DevOps.pdf"],
  ["Multi Cloud Management", "multi-cloud-management.pdf"],
  ["Serverless Computing", "serverless_computing.pdf"]
]);

addSemesterResources("btech-cse-cloud", 8, [
  ["Cloud Computing Paradigms", "Cloud Computing Paradigms.pdf"],
  ["Cloud Computing Principles and Paradigms", "CLOUD COMPUTING Principles and Paradigms.pdf"],
  ["Cloud Governance", "Cloud Governance.pdf"]
]);

// BTECH - CSE CORE

addSemesterResources("btech-cse-core", 1, [
  ["Basic Electrical Engineering", "Basic Electrical Engineering.pdf"],
  ["C Programming", "C_Programming.pdf"],
  ["Engineering Physics", "Engineering_Physics.pdf"],
  ["Fundamentals of Computers", "Fundamentals of Computers.pdf"],
  ["Mathematics", "mathematics.pdf"]
]);

addSemesterResources("btech-cse-core", 2, [
  ["DSA", "Dsa.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Object Oriented Programming", "OBJECT_ORIENTED_PROGRAMMING.pdf"]
]);

addSemesterResources("btech-cse-core", 3, [
  ["Computer Organization and Architecture", "Computer-Organization-Architecture.pdf"],
  ["Managing Database", "MANAGING_DATABASE.pdf"],
  ["Object Oriented Analysis and Design", "Object.Oriented.Analysis.and.Design..pdf"],
  ["Operating System Concepts", "Operating-System-Concepts.pdf"]
]);

addSemesterResources("btech-cse-core", 4, [
  ["Algorithms", "Algorithms.pdf"],
  ["Computation", "Computation.pdf"],
  ["Computer Networks", "COMPUTER_NETWORKS.pdf"],
  ["Probability and Statistics", "probality_and_statistics.pdf"],
  ["Software Engineering", "SOFTWARE_ENGINEERING.pdf"]
]);

addSemesterResources("btech-cse-core", 5, [
  ["Artificial Intelligence", "Artificial Intelligence.pdf"],
  ["Compiler Design", "compilerDesign.pdf"],
  ["Computer Graphics", "COMPUTER_GRAPHICS.pdf"]
]);

addSemesterResources("btech-cse-core", 6, [
  ["Cloud Computing", "CLOUD COMPUTING.pdf"],
  ["Distributed Systems", "distributed_systems.pdf"],
  ["Information Security", "information_security.pdf"],
  ["Machine Learning", "Machine Learning.pdf"]
]);

addSemesterResources("btech-cse-core", 7, [
  ["Advanced Database Systems", "advanced_database_systems.pdf"],
  ["Big Data", "big_data.pdf"],
  ["Mobile App Development", "Mobile App Development.pdf"],
  ["Software Testing", "SOFTWARE_TESTINg.pdf"]
]);

addSemesterResources("btech-cse-core", 8, [
  ["Information Retrieval", "information_retrieval.pdf"],
  ["Project Management", "PROJECT_MANAGEMENT.pdf"],
  ["Research Methodology", "Research Methodology.pdf"]
]);

// BTECH - CSE CYBERSECURITY

addSemesterResources("btech-cse-cybersecurity", 1, [
  ["Calculus 1", "calculus-1.pdf"],
  ["ECE", "ece.pdf"],
  ["Physics 1", "Physics-1.pdf"],
  ["Think Python", "thinkpython.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 2, [
  ["DSA", "Dsa.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Object Oriented Programming", "OBJECT_ORIENTED_PROGRAMMING.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 3, [
  ["Computer Networks", "COMPUTER_NETWORKS.pdf"],
  ["Database Management Systems", "Database-Management-Systems.pdf"],
  ["Operating System", "Operating-System.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 4, [
  ["Cryptology", "cryptology.pdf"],
  ["Network Security", "network_security.pdf"],
  ["Principles of System Administration", "principles-of-system-administration.pdf"],
  ["Web Development", "Web Development.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 5, [
  ["Cryptography", "cryptography.pdf"],
  ["Hacking", "hacking.pdf"],
  ["Information Security", "information_security.pdf"],
  ["Security Operation", "security_operation.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 6, [
  ["Attack and Defence", "attack_and_defence.pdf"],
  ["Digital Forensics", "digital_forensics.pdf"],
  ["Operating Systems Virtualisation", "Operating_Systems_Virtualisation.pdf"],
  ["Secure Software Development", "secure_software_development.pdf"],
  ["Web Application Security", "Web Application Security (1).pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 7, [
  ["Cloud Security", "cloud_security.pdf"],
  ["Malware Analysis", "malwareanalysis.pdf"],
  ["Penetration Testing", "Penetration-Testing.pdf"],
  ["Security Incident Handling", "security_incident_handeling.pdf"]
]);

addSemesterResources("btech-cse-cybersecurity", 8, [
  ["Cyber Security Affecting", "CYBER SECURITY AFFECTING.pdf"],
  ["Cyber Law and Ethics", "cyber_law_and_ethics.pdf"],
  ["Penetration Testing", "peneteration_testing.pdf"],
  ["Security and Risk Management", "security_and_risk_managment.pdf"],
  ["Vulnerability", "vulnerability.pdf"]
]);

// BTECH - CSE DATA SCIENCE

addSemesterResources("btech-cse-data-science", 1, [
  ["Basic Electrical Engineering", "Basic Electrical Engineering.pdf"],
  ["Engineering Physics", "Engineering_Physics.pdf"],
  ["Fundamentals of Computers", "Fundamentals of Computers.pdf"],
  ["Mathematics", "mathematics.pdf"]
]);

addSemesterResources("btech-cse-data-science", 2, [
  ["Calculus 2", "calculus-2.pdf"],
  ["Data Structures", "Data_Structures.pdf"],
  ["Discrete Mathematics", "discrete_mathematics.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Think Java", "thinkjava.pdf"]
]);

addSemesterResources("btech-cse-data-science", 3, [
  ["Database System", "database_system.pdf"],
  ["DSA", "Dsa.pdf"],
  ["Operating System", "Operating-System.pdf"],
  ["Statistical Methods", "Statistical Methods.pdf"]
]);

addSemesterResources("btech-cse-data-science", 4, [
  ["Algorithms", "Algorithms.pdf"],
  ["Computer Networks", "COMPUTER_NETWORKS.pdf"],
  ["Numerical Methods", "numerical_methods.pdf"],
  ["Software Engineering", "SOFTWARE_ENGINEERING.pdf"],
  ["Theory of Computation", "TheoryOfComputation.pdf"]
]);

addSemesterResources("btech-cse-data-science", 5, [
  ["Data Science", "data_science.pdf"],
  ["Data Mining", "data-mining.pdf"],
  ["Python for Data Analysis", "Python-for-Data-Analysis.pdf"]
]);

addSemesterResources("btech-cse-data-science", 6, [
  ["Big Data", "big_data.pdf"],
  ["Data Visualization", "Data_Visualization.pdf"],
  ["Data Warehousing and Data Mining", "DATAWARE_HOUSING_AND_DATAMINING.pdf"],
  ["Machine Learning", "Machine Learning.pdf"]
]);

addSemesterResources("btech-cse-data-science", 7, [
  ["Data Engineering", "Data Engineering.pdf"],
  ["Data Analytics for Business", "data_analytics_for_business.pdf"],
  ["Natural Language Processing", "natural_language_processing.pdf"],
  ["Time Series", "time_series.pdf"]
]);

addSemesterResources("btech-cse-data-science", 8, [
  ["Business Intelligence", "BUSINESS_INTELLIGENCE.pdf"],
  ["Data Science", "Data Science.pdf"],
  ["Predictive Analytics", "predictive-analytics.pdf"]
]);

// BTECH - CSE IOT

addSemesterResources("btech-cse-iot", 1, [
  ["Calculus 1", "calculus-1.pdf"],
  ["ECE", "ece.pdf"],
  ["Physics 1", "Physics-1.pdf"],
  ["Think Python", "thinkpython.pdf"]
]);

addSemesterResources("btech-cse-iot", 2, [
  ["Digital Logic", "digital_logic.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Microprocessor and Microcontroller", "microprocessor_and_microcontroller.pdf"]
]);

addSemesterResources("btech-cse-iot", 3, [
  ["Computer Networks", "COMPUTER_NETWORKS.pdf"],
  ["Embedded Systems", "embedded_systems.pdf"],
  ["Operating System", "OPERATING_SYSTEM.pdf"],
  ["Python", "python.pdf"]
]);

addSemesterResources("btech-cse-iot", 4, [
  ["Database Management Systems", "Database-Management-Systems.pdf"],
  ["Sensors and Actuators", "SENSORS-AND-ACTUATORS.pdf"],
  ["Wireless Communication", "wireless_communication.pdf"]
]);

addSemesterResources("btech-cse-iot", 5, [
  ["Internet of Things", "Internet-of-things.pdf"],
  ["IoT Architecture", "iot_arvhitecture.pdf"],
  ["Programming Embedded Systems", "Programming_Embedded_Systems.pdf"],
  ["Wireless Sensor Networks", "Wireless Sensor Networks.pdf"]
]);

addSemesterResources("btech-cse-iot", 6, [
  ["Arduino Raspberry Pi Pico", "arduino_raspberry_pi_pico.pdf"],
  ["Edge Computing", "edge-computing.pdf"],
  ["Enabling IoT", "enabling-IOT.pdf"]
]);

addSemesterResources("btech-cse-iot", 7, [
  ["Industrial IoT", "industrial_iot.pdf"],
  ["IoT Analytics", "iot_analytics.pdf"],
  ["IoT Fundamental", "iot_fundamental.pdf"],
  ["IoT Security", "IoT-Security.pdf"],
  ["Smart Material Systems", "smart_material_systems.pdf"]
]);

addSemesterResources("btech-cse-iot", 8, [
  ["Internet of Things", "Internet-of-things.pdf"],
  ["Project Management", "PROJECT_MANAGEMENT.pdf"],
  ["Projects", "projects.pdf"]
]);

// BTECH - CSE SOFTWARE ENGINEERING

addSemesterResources("btech-cse-software-engineering", 1, [
  ["Basic Electrical Engineering", "Basic Electrical Engineering.pdf"],
  ["C Programming", "C_Programming.pdf"],
  ["Engineering Physics", "Engineering_Physics.pdf"],
  ["Fundamentals of Computers", "Fundamentals of Computers.pdf"],
  ["Mathematics", "mathematics.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 2, [
  ["DSA", "Dsa.pdf"],
  ["Engineering Chemistry", "Engg Chemistry.pdf"],
  ["Engineering Mathematics II", "engineering-mathematics-ii.pdf"],
  ["Object Oriented Programming", "OBJECT_ORIENTED_PROGRAMMING.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 3, [
  ["Computer Organization", "Computer Organization.pdf"],
  ["Discrete Math", "discrete_math.pdf"],
  ["DSA", "dsa.pdf"],
  ["Linear Algebra and Probability", "linear_algebra_and_probability.pdf"],
  ["Operating System Concepts", "Operating-System-Concepts.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 4, [
  ["Computer Networks", "computer-networks.pdf"],
  ["Database Design", "Database-Design.pdf"],
  ["Operating Systems", "operating_systems.pdf"],
  ["Software Engineering", "SOFTWARE_ENGINEERING.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 5, [
  ["Design Patterns", "design_patterns.pdf"],
  ["Object Oriented Analysis and Design", "object_oriented_analysis_and_design.pdf"],
  ["Software Architecture", "software_architecture.pdf"],
  ["Software Requirements", "software_requirements.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 6, [
  ["Agile Software Development", "agile_software_development.pdf"],
  ["DevOps", "devops.pdf"],
  ["Software Testing and Quality Assurance", "SOFTWARE_TESTING_AND_QUALITY_ASSURANCE.pdf"],
  ["Version Control with Git", "Version Control with GIT.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 7, [
  ["Distributed Systems", "distributed_systems.pdf"],
  ["Software Architecture for Developers", "sddconf2014-software-architecture-for-developers-extract.pdf"],
  ["Secure Software Development", "secure_software_development.pdf"],
  ["Software Project Management", "SOFTWARE_PROJECT_MANAGEMENT.pdf"]
]);

addSemesterResources("btech-cse-software-engineering", 8, [
  ["Reliability Engineering", "Reliability-Engineering.pdf"],
  ["Software Metrics", "software_metrics.pdf"],
  ["Software Project Management", "SOFTWARE_PROJECT_MANAGEMENT.pdf"],
  ["Software Evolution and Maintenance", "software-evolution-and-maintenance (1).pdf"]
]);

// BTECH - CIVIL ENGINEERING

addSemesterResources("btech-civil", 1, [
  ["Calculus Volume 1", "calculus-volume-1.pdf"],
  ["Electric Circuits", "electric circuits.pdf"],
  ["Engineering Mechanics", "Engineering Mechanics.pdf"],
  ["Physics I", "Physics-I.pdf"]
]);

addSemesterResources("btech-civil", 2, [
  ["Calculus Volume 2", "calculus-volume-2.pdf"],
  ["Engineering Drawing and Design", "Engineering Drawing and design.pdf"],
  ["Environmental Engineering", "environmental-engineering.pdf"],
  ["Fluid Mechanics", "Fluid Mechanics.pdf"],
  ["Strength of Materials", "strength_of_materials.pdf"],
  ["Surveying and Levelling", "Surveying_and_Levelling.pdf"]
]);

addSemesterResources("btech-civil", 3, [
  ["Computational Hydraulics", "computational-hydraulics.pdf"],
  ["Concrete Technology", "Concrete Technology.pdf"],
  ["Geotechnical Engineering", "geotechnical-engineering.pdf"]
]);

addSemesterResources("btech-civil", 4, [
  ["Geotechnical Engineering", "geotechnical-engineering.pdf"],
  ["Strength of Materials", "strength_of_materials.pdf"],
  ["Surveying and Levelling", "Surveying_and_Levelling.pdf"],
  ["Transportation Engineering", "transportation_engg.pdf"]
]);

addSemesterResources("btech-civil", 5, [
  ["Introduction to Environmental Engineering", "introduction-to-environmental-engineering.pdf"],
  ["Transportation Engineering", "tranportation_engineering.pdf"]
]);

addSemesterResources("btech-civil", 6, [
  ["Construction Management", "Construction_management.pdf"],
  ["Design of Steel Structures", "Design of Steel Structures.pdf"],
  ["Transportation Engineering", "transportation_engineering.pdf"]
]);

addSemesterResources("btech-civil", 7, [
  ["Basic Principles of Remote Sensing", "Basics Principles of Remote Sensing.pdf"],
  ["Seismicity", "Seismicity.pdf"],
  ["Structural Analysis", "structural analysis.pdf"]
]);

addSemesterResources("btech-civil", 8, [
  ["Advanced Foundation Engineering", "advanced-foundation-engineering.pdf"],
  ["Earthwork Simulation", "Earthwork Simulation.pdf"],
  ["Management Principles", "management_principles.pdf"],
  ["Sustainable Construction", "sustainable_construction.pdf"]
]);

// BTECH - ELECTRICAL ENGINEERING

addSemesterResources("btech-electrical", 1, [
  ["Calculus Volume 1", "calculus-volume-1.pdf"],
  ["Electric Circuits", "electric circuits.pdf"],
  ["Engineering Mechanics", "Engineering Mechanics.pdf"],
  ["Physics I", "Physics-I.pdf"]
]);

addSemesterResources("btech-electrical", 2, [
  ["Calculus Volume 2", "calculus-volume-2.pdf"],
  ["Engineering Drawing and Design", "Engineering Drawing and design.pdf"],
  ["Environmental Engineering", "environmental-engineering.pdf"]
]);

addSemesterResources("btech-electrical", 3, [
  ["Analog Electronics", "AnalogElectronics.pdf"],
  ["Electromagnetic Field Theory", "Electromagnetic-Field-Theory.pdf"],
  ["Principles of Electrical Measurement", "principles-of-electrical-measurement.pdf"]
]);

addSemesterResources("btech-electrical", 4, [
  ["Digital Electronics", "Digital Electronics.pdf"],
  ["Digital Design", "Digital-Design.pdf"],
  ["Digital Electronics", "DigitalElectronics.pdf"],
  ["Electrical Machines", "electrical_machines.pdf"],
  ["Power Electronics", "power elecgtronics.pdf"]
]);

addSemesterResources("btech-electrical", 5, [
  ["Control Systems", "control_systems.pdf"],
  ["Electrical Machines", "ELECTRICAL MACHINES.pdf"],
  ["Electrical Power Systems", "electrical-power-systems.pdf"],
  ["Microprocessors and Microcontrollers", "MicroprocessorsandMicrocontrollers.pdf"]
]);

addSemesterResources("btech-electrical", 6, [
  ["Electrical Machine Design", "electrical_machine_design.pdf"],
  ["Electrical Machine Design", "electrical-machine-design-byvrajini-1.pdf"]
]);

addSemesterResources("btech-electrical", 7, [
  ["High Voltage Engineering", "high_voltage_engineering.pdf"],
  ["Renewable Energy Systems", "renewable_energy_systems.pdf"],
  ["Smart Grid", "smart_grid.pdf"]
]);

addSemesterResources("btech-electrical", 8, [
  ["AI in Power System Optimization", "ai_in_power_system_optimizaion.pdf"],
  ["Electric Vehicle", "electrics_vehicle.pdf"],
  ["Energy Management", "Energy Management.pdf"]
]);

// BTECH - MECHANICAL ENGINEERING

addSemesterResources("btech-mechanical", 1, [
  ["Electric Circuits", "electric circuits.pdf"],
  ["Engineering Physics", "Engineering_Physics.pdf"],
  ["Mathematics", "mathematics.pdf"],
  ["Physics I", "Physics-I.pdf"]
]);

addSemesterResources("btech-mechanical", 2, [
  ["Calculus Volume 2", "calculus-volume-2.pdf"],
  ["Engineering Drawing and Design", "Engineering Drawing and design.pdf"],
  ["Engineering Graphics", "ENGINEERING GRAPHICS.pdf"],
  ["Environmental Engineering", "environmental-engineering.pdf"],
  ["Fluid Mechanics", "Fluid Mechanics.pdf"]
]);

addSemesterResources("btech-mechanical", 3, [
  ["Manufacturing Processes", "Manufacturing Processes.pdf"],
  ["Material Science", "material science.pdf"]
]);

addSemesterResources("btech-mechanical", 4, [
  ["Fluid Mechanics", "Fluid Mechanics.pdf"],
  ["Materials for Engineering", "Materials for engineering.pdf"],
  ["Theory of Machines", "Theory of Machines.pdf"],
  ["Thermodynamics", "thermodynamics.pdf"]
]);

addSemesterResources("btech-mechanical", 5, [
  ["Industrial Engineering and Management", "industrial_engineering_and_management.pdf"],
  ["Manufacturing Technology", "manufacturing_technology.pdf"]
]);

addSemesterResources("btech-mechanical", 6, [
  ["Machine Design", "Machine-Design.pdf"],
  ["Mechanical Vibrations", "mechanical_vibrations.pdf"],
  ["Principles of CAD CAM", "principles_of_CAD-CAM.pdf"]
]);

addSemesterResources("btech-mechanical", 7, [
  ["Computational Fluid Dynamics", "computational-fluid-dynamics.pdf"],
  ["Finite Element", "Finite Element.pdf"],
  ["Motor Vehicle Engineering", "Motor Vehicle Engineering.pdf"],
  ["Robotics and Automation", "robotics_and_automation.pdf"]
]);

addSemesterResources("btech-mechanical", 8, [
  ["Advanced Manufacturing Technology", "advance_manufacturing_technology.pdf"],
  ["Industrial Automation", "industrial_automation.pdf"],
  ["Renewable Energy Systems", "renewable_energy_systems.pdf"]
]);

// HELPER FUNCTIONS

export function getFields() {
  return academicResources.fields;
}

export function getProgrammes(fieldId = null) {
  if (!fieldId) {
    return academicResources.programmes;
  }

  return academicResources.programmes.filter(
    programme => programme.fieldId === fieldId
  );
}

export function getSemesters(programmeId) {
  return academicResources.semesters.filter(
    semester => semester.programmeId === programmeId
  );
}

export function getResources(programmeId, semesterNumber) {
  const semesterId = `${programmeId}-semester-${semesterNumber}`;

  return academicResources.resources.filter(
    resource =>
      resource.programmeId === programmeId &&
      resource.semesterId === semesterId
  );
}

export function searchResources(searchText) {
  const query = searchText.trim().toLowerCase();

  if (!query) return [];

  return academicResources.resources.filter(
    resource => resource.title.toLowerCase().includes(query)
  );
}

export function getResourceById(resourceId) {
  return academicResources.resources.find(
    resource => resource.id === resourceId
  ) || null;
}

export function getAvailablePDFs() {
  return academicResources.resources.filter(
    resource => resource.fileUrl !== null
  );
}

export default academicResources;
