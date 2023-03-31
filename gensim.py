from gensim.summarization import keywords
text = """Overview

SCCI is seeking a System Security Analyst to join our team! The successful candidate will support our cybersecurity engineering and RMF package activities. This position is for future work expected to be available in early 2023.  This position is located in Dahlgren, VA.

 

Responsibilities:

Perform vulnerability analysis, risk analysis, scanning for viruses and other software that is detrimental to IT systems, accreditation of systems, and audits
Conduct integration, testing operations, and maintenance of information systems security
Maintain the accreditation status for assigned packages
Support Continuous Monitoring phase of the RMF process
Support Testing and Documentation of systems at defined intervals
Ensure all security controls are reviewed and documented in accordance with the approved System Level Continuous Monitoring (SLCM) strategy outlined for the systems
Maintain the system Plan of Action and Milestones (POA&Ms) for these systems and ensures all system vulnerabilities are documented in the eMASS portal for review by the approving authority
Support discussions and action resolutions during concurrent reviews of the Security Authorization Package
Assist the ISSE in the documenting a system from an IA perspective using Microsoft Office including MS Word, MS Excel and MS Visio and other appropriate tools
Essential Skills and Experience:

Must be a U.S. Citizen and have an ACTIVE TOP SECRET SECURITY CLEARANCE
Bachelor of Science (BS) degree in an engineering, scientific, technical discipline or equivalent experience
Per DoD Directive 8570.1M or successor, this position requires IAM Level II (or equivalent) or higher
IT specific experience with the DoD or Navy to include vulnerability analysis, risk analysis, scanning for viruses and other software that is detrimental to IT systems, accreditation of systems, and audits
Must possess an in depth understanding of computer security, military system specifications, DoD IA policies for both Land Based and afloat/tactical systems, and the ability to communicate clearly and succinctly in written and oral presentations
Experience conducting integration and testing operations and maintenance of information systems security
Experience maintaining the accreditation status for assigned packages
Experience supporting Continuous Monitoring phase of the RMF process
Experience testing and documenting systems
Ensured all security controls are reviewed and documented in accordance with the approved SLCM strategy outlined for the systems
Maintained the system POA&Ms for these systems and ensures all system vulnerabilities are documented in the eMASS portal for review by the approving authority
 

SCCI is committed to providing a comprehensive and competitive benefits package to meet the needs of employees and their families. EOE of Minorities, Females, Veterans, Disabilities."""

print(keywords(text))
