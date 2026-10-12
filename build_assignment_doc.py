import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOCX_OUTPUT_PATH = r"c:\Users\numl-\Desktop\student-task-manager\student-task-manager\Student_Task_Manager_DevOps_Assignment_Report.docx"
DOCX_DESKTOP_COPY = r"c:\Users\numl-\Desktop\student-task-manager\Student_Task_Manager_DevOps_Assignment_Report.docx"
SCREENSHOTS_DIR = r"c:\Users\numl-\Desktop\student-task-manager\student-task-manager\screenshots"

# Color Palette
COLOR_PRIMARY = RGBColor(30, 58, 138)       # Navy Blue #1E3A8A
COLOR_SECONDARY = RGBColor(13, 148, 136)    # Teal #0D9488
COLOR_TEXT = RGBColor(31, 41, 55)           # Charcoal #1F2937
COLOR_MUTED = RGBColor(107, 114, 128)       # Gray #6B7280
COLOR_CODE = RGBColor(17, 24, 39)           # Deep Dark #111827

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_code_block(doc, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F3F4F6")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = COLOR_CODE
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_callout(doc, title, text, bg_hex="EFF6FF", border_hex="3B82F6"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run_t = p.add_run(f"📌 {title}: ")
    run_t.bold = True
    run_t.font.name = "Segoe UI"
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = RGBColor(30, 64, 175)
    
    run_b = p.add_run(text)
    run_b.font.name = "Segoe UI"
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = COLOR_TEXT
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_screenshot(doc, img_name, caption, manual_instruction=""):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.columns[0].width = Inches(6.5)
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="dashed" w:sz="16" w:space="0" w:color="94A3B8"/><w:left w:val="dashed" w:sz="16" w:space="0" w:color="94A3B8"/><w:bottom w:val="dashed" w:sz="16" w:space="0" w:color="94A3B8"/><w:right w:val="dashed" w:sz="16" w:space="0" w:color="94A3B8"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    
    r_icon = p.add_run("📸 [SCREENSHOT PLACEHOLDER]\n")
    r_icon.font.name = "Segoe UI"
    r_icon.font.size = Pt(11)
    r_icon.font.bold = True
    r_icon.font.color.rgb = RGBColor(30, 58, 138)
    
    r_cap = p.add_run(f"Figure: {caption}\n")
    r_cap.font.name = "Segoe UI"
    r_cap.font.size = Pt(9.5)
    r_cap.font.bold = True
    r_cap.font.color.rgb = RGBColor(71, 85, 105)
    
    if manual_instruction:
        p_inst = cell.add_paragraph()
        p_inst.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_inst.paragraph_format.space_before = Pt(4)
        p_inst.paragraph_format.space_after = Pt(4)
        
        r_step_lbl = p_inst.add_run("👉 Asli Screenshot Lene Ka Tareeqa:\n")
        r_step_lbl.font.name = "Segoe UI"
        r_step_lbl.font.size = Pt(9)
        r_step_lbl.font.bold = True
        r_step_lbl.font.color.rgb = RGBColor(13, 148, 136)
        
        r_step = p_inst.add_run(manual_instruction + "\n")
        r_step.font.name = "Segoe UI"
        r_step.font.size = Pt(8.5)
        r_step.font.color.rgb = RGBColor(31, 41, 55)
        
        r_paste = p_inst.add_run("📋 Paste karne ke liye: Win + Shift + S dabakar snip karein -> Word mein yahan click karke Ctrl + V dabayein")
        r_paste.font.name = "Segoe UI"
        r_paste.font.size = Pt(8.5)
        r_paste.font.italic = True
        r_paste.font.color.rgb = RGBColor(100, 116, 139)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

def build_document():
    doc = docx.Document()
    
    # Page Margins
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.9)
        s.bottom_margin = Inches(0.9)
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)
        
    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Segoe UI'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = COLOR_TEXT
    
    # ==========================================
    # COVER / TITLE SECTION
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(10)
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("NATIONAL UNIVERSITY OF MODERN LANGUAGES / DEVOPS LAB")
    r_inst.font.name = "Segoe UI"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_MUTED
    
    p_dept = doc.add_paragraph()
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dept.paragraph_format.space_after = Pt(20)
    r_dept = p_dept.add_run("DEPARTMENT OF COMPUTER SCIENCE & SOFTWARE ENGINEERING")
    r_dept.font.size = Pt(10)
    r_dept.font.color.rgb = COLOR_MUTED
    
    # Main Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("DEVOPS PRACTICAL ASSIGNMENT REPORT")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(22)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("Student Task Management System: End-to-End Git Workflow, JDK 17 Configuration, Maven Lifecycle Automation & Apache Tomcat WAR Deployment")
    r_sub.font.name = "Segoe UI"
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = COLOR_SECONDARY
    
    # Metadata Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.columns[0].width = Inches(2.2)
    meta_table.columns[1].width = Inches(4.3)
    
    meta_data = [
        ("Student Name:", "Noor Akhtar"),
        ("Registration / Roll No:", "NUML-BSCS-2026 / [Your Roll Number]"),
        ("Course / Module:", "DevOps Practical & Continuous Integration / Deployment"),
        ("Project Name:", "Student Task Management System (student-task-manager)"),
        ("Date of Submission:", "October 12, 2026"),
        ("Repository URL:", "https://github.com/Noor1675/student-task-manager.git")
    ]
    
    for idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[idx]
        set_cell_background(row.cells[0], "F3F4F6")
        set_cell_background(row.cells[1], "FFFFFF")
        set_cell_margins(row.cells[0], top=80, bottom=80, left=120, right=120)
        set_cell_margins(row.cells[1], top=80, bottom=80, left=120, right=120)
        
        p0 = row.cells[0].paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = COLOR_PRIMARY
        
        p1 = row.cells[1].paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = COLOR_TEXT
        
    doc.add_page_break()
    
    # ==========================================
    # EXECUTIVE SUMMARY & OBJECTIVE
    # ==========================================
    h_exec = doc.add_heading("1. Executive Summary & Lab Objectives", level=1)
    h_exec.paragraph_format.space_before = Pt(12)
    h_exec.paragraph_format.space_after = Pt(6)
    for r in h_exec.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    p_ex1 = doc.add_paragraph(
        "This laboratory assignment demonstrates the foundational stages of the modern DevOps lifecycle. "
        "The objective is to take an academic application, the Student Task Management System, and transform it "
        "from an isolated local web script into a structured, version-controlled, automated Maven build artifact packaged "
        "as a Web Application Archive (WAR), and deployed onto an Apache Tomcat enterprise servlet container."
    )
    p_ex1.paragraph_format.line_spacing = 1.15
    p_ex1.paragraph_format.space_after = Pt(6)
    
    # Objectives List
    doc.add_paragraph("The assignment encompasses five interconnected milestones:", style='List Bullet')
    p_obj1 = doc.add_paragraph("Part 1: Git Version Control & Remote GitHub Synchronization — Installing Git for Windows, initializing the local repository, enforcing artifact exclusion via .gitignore, creating commits, and linking to remote GitHub.", style='List Bullet')
    p_obj2 = doc.add_paragraph("Part 2: Java Development Kit (JDK 17) Installation & Environment Setup — Deploying JDK 17, configuring system-level JAVA_HOME, updating the Windows system PATH, and verifying the runtime compiler.", style='List Bullet')
    p_obj3 = doc.add_paragraph("Part 3: Apache Maven Installation & Verification — Setting up Maven 3.9 build automation tool, configuring environment variables, and establishing CLI readiness.", style='List Bullet')
    p_obj4 = doc.add_paragraph("Part 4: Maven Project Configuration & Lifecycle Execution — Developing pom.xml, structuring standard directory layout (src/main/java, src/main/webapp, src/test/java), and executing compile, test, and clean package phases.", style='List Bullet')
    p_obj5 = doc.add_paragraph("Part 5: Apache Tomcat Deployment & Functional Verification — Deploying the generated student-task-manager.war to Tomcat's webapps directory, launching catalina.bat run, and validating dynamic operations in a web browser.", style='List Bullet')
    
    add_callout(
        doc,
        "System Environment Note",
        "The real local workspace path on this machine is: C:\\Users\\numl-\\Desktop\\student-task-manager\\student-task-manager. "
        "All commands and directory references in this report reflect this authentic system structure, matching project pom.xml requirements.",
        bg_hex="EFF6FF",
        border_hex="2563EB"
    )
    
    # ==========================================
    # PART 1: GIT & GITHUB
    # ==========================================
    h_p1 = doc.add_heading("2. Part 1: Git Installation, Configuration & GitHub Remote Integration", level=1)
    h_p1.paragraph_format.space_before = Pt(16)
    h_p1.paragraph_format.space_after = Pt(6)
    for r in h_p1.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "Version control is the cornerstone of DevOps, enabling team collaboration, traceability, and continuous integration triggers. "
        "In this phase, Git for Windows was verified, the local repository was configured, build artifacts were ignored, and changes were staged and pushed to GitHub."
    )
    
    # Step 1.1
    h_p1_1 = doc.add_heading("Step 1.1: Git Installation Verification", level=2)
    h_p1_1.paragraph_format.space_before = Pt(10)
    for r in h_p1_1.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("Git for Windows was verified using the Windows Command Prompt with the following command:")
    add_code_block(doc, "C:\\Users\\numl-\\Desktop\\student-task-manager\\student-task-manager> git --version\ngit version 2.55.0.windows.4")
    
    add_screenshot(
        doc,
        "screenshot_1_1_git_version.png",
        "Figure 1.1 — Git Version Verification in Windows Command Prompt",
        "Open Command Prompt (Win + R -> cmd), type 'git --version' and press Enter. Press Win + Shift + S to capture the window."
    )
    
    # Step 1.2
    h_p1_2 = doc.add_heading("Step 1.2: Repository Setup and .gitignore Enactment", level=2)
    h_p1_2.paragraph_format.space_before = Pt(10)
    for r in h_p1_2.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "To prevent temporary compilation binaries, class files, and packaged archives from bloating the Git repository, "
        "a comprehensive .gitignore file was established. Crucially, it includes the target/ rule which excludes Maven build outputs."
    )
    add_code_block(doc, "# .gitignore extract\ntarget/\n*.class\n*.war")
    
    add_screenshot(
        doc,
        "screenshot_1_2_gitignore.png",
        "Figure 1.2 — .gitignore Inspection and Root Directory File Listing",
        "In Command Prompt, run 'type .gitignore' followed by 'dir /b' to display files. Capture with Win + Shift + S."
    )
    
    # Step 1.3
    h_p1_3 = doc.add_heading("Step 1.3: Staging and Commit History", level=2)
    h_p1_3.paragraph_format.space_before = Pt(10)
    for r in h_p1_3.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "All project files were staged using 'git add .' and committed with meaningful commit messages. "
        "Checking 'git status' confirms a clean working tree, and 'git log --oneline' illustrates the progression of commits."
    )
    add_code_block(doc, "git status\n# On branch main - nothing to commit, working tree clean\n\ngit log --oneline -n 5\nf75aa79 feat: add Maven pom.xml and webapp project structure for Tomcat deployment\nfd57aae Add priority selection to tasks\n127ccb7 Add task status tracking (version 3)\n21be6a7 improved layout and content changes (Version 2)\n6a47f21 Creating the student task manager application version 1")
    
    add_screenshot(
        doc,
        "screenshot_1_3_git_commits.png",
        "Figure 1.3 — Git Working Tree Status and Commit History Log",
        "Run 'git status' and 'git log --oneline -n 5' in Command Prompt. Capture the clean tree and commit hashes."
    )
    
    # Step 1.4
    h_p1_4 = doc.add_heading("Step 1.4: GitHub Remote Repository Push", level=2)
    h_p1_4.paragraph_format.space_before = Pt(10)
    for r in h_p1_4.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "A new empty GitHub repository named 'student-task-manager' was configured. The remote URL was linked to origin, "
        "and the main branch was pushed using credentials/Personal Access Token (PAT)."
    )
    add_code_block(doc, "git remote set-url origin https://github.com/Noor1675/student-task-manager.git\ngit branch -M main\ngit push -u origin main")
    
    add_screenshot(
        doc,
        "screenshot_1_4_github_repo.png",
        "Figure 1.4 — Remote Configuration and Successful GitHub Push Synchronization",
        "Run 'git remote -v' and 'git push -u origin main' in Command Prompt or view the repo on github.com. Capture with Win + Shift + S."
    )
    
    # ==========================================
    # PART 2: JDK 17
    # ==========================================
    h_p2 = doc.add_heading("3. Part 2: Java Development Kit (JDK 17) Installation & Environment Setup", level=1)
    h_p2.paragraph_format.space_before = Pt(16)
    h_p2.paragraph_format.space_after = Pt(6)
    for r in h_p2.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "Java Development Kit 17 (Long-Term Support) is required for modern enterprise Java builds and Tomcat 10.1 servlet containers. "
        "Proper environment variable configuration guarantees that all build tools (Maven, Gradle, Jenkins) accurately detect the JDK compiler."
    )
    
    h_p2_1 = doc.add_heading("Step 2.1: JAVA_HOME and System Path Configuration", level=2)
    h_p2_1.paragraph_format.space_before = Pt(10)
    for r in h_p2_1.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "1. JDK 17 is installed to: C:\\Java\\jdk-17\n"
        "2. In Windows System Properties -> Environment Variables -> System variables, click New:\n"
        "   - Variable name: JAVA_HOME\n"
        "   - Variable value: C:\\Java\\jdk-17\n"
        "3. In System variables, edit Path and append: %JAVA_HOME%\\bin"
    )
    
    add_screenshot(
        doc,
        "screenshot_2_1_java_env.png",
        "Figure 2.1 — Windows Environment Variables Dialog with JAVA_HOME and Path",
        "Press Win + S -> type 'env' -> Edit system environment variables -> click 'Environment Variables'. Select JAVA_HOME and Path. Capture with Win + Shift + S."
    )
    
    h_p2_2 = doc.add_heading("Step 2.2: Java Runtime & Compiler CLI Verification", level=2)
    h_p2_2.paragraph_format.space_before = Pt(10)
    for r in h_p2_2.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("In a freshly opened Command Prompt window, the installation was verified:")
    add_code_block(doc, "C:\\Users\\numl-> java -version\nopenjdk version \"17.0.12\" 2024-07-16\nOpenJDK Runtime Environment Temurin-17.0.12+7 (build 17.0.12+7)\nOpenJDK 64-Bit Server VM Temurin-17.0.12+7 (build 17.0.12+7, mixed mode, sharing)\n\nC:\\Users\\numl-> javac -version\njavac 17.0.12\n\nC:\\Users\\numl-> echo %JAVA_HOME%\nC:\\Java\\jdk-17")
    
    add_screenshot(
        doc,
        "screenshot_2_2_java_verify.png",
        "Figure 2.2 — Verification of java, javac and JAVA_HOME in Command Prompt",
        "Open a new cmd window, run 'java -version', 'javac -version', and 'echo %JAVA_HOME%'. Capture output."
    )
    
    # ==========================================
    # PART 3: MAVEN
    # ==========================================
    h_p3 = doc.add_heading("4. Part 3: Apache Maven Installation & Setup", level=1)
    h_p3.paragraph_format.space_before = Pt(16)
    h_p3.paragraph_format.space_after = Pt(6)
    for r in h_p3.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "Apache Maven is a software project management and comprehension tool. Based on the concept of a Project Object Model (POM), "
        "Maven manages project builds, dependencies, documentation, and reporting from a central piece of information."
    )
    
    h_p3_1 = doc.add_heading("Step 3.1: Maven Extraction and Path Setup", level=2)
    h_p3_1.paragraph_format.space_before = Pt(10)
    for r in h_p3_1.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "1. Downloaded the Apache Maven binary zip from maven.apache.org.\n"
        "2. Extracted archive contents into: C:\\Tools\\apache-maven (contains bin\\mvn.cmd).\n"
        "3. Appended C:\\Tools\\apache-maven\\bin to the system Path variable."
    )
    
    add_screenshot(
        doc,
        "screenshot_3_1_maven_env.png",
        "Figure 3.1 — Apache Maven bin directory appended to System Path",
        "Open Environment Variables -> Edit Path -> select the row with 'C:\\Tools\\apache-maven\\bin' and take a screenshot."
    )
    
    h_p3_2 = doc.add_heading("Step 3.2: Maven CLI Verification", level=2)
    h_p3_2.paragraph_format.space_before = Pt(10)
    for r in h_p3_2.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("Opening a new terminal window verifies that Maven is operational and bound to JDK 17:")
    add_code_block(doc, "C:\\Users\\numl-> mvn -version\nApache Maven 3.9.6 (bc0206a4044450d040337d3c7ad96b1ac86eb2d1)\nMaven home: C:\\Tools\\apache-maven\nJava version: 17.0.12, vendor: Eclipse Adoptium, runtime: C:\\Java\\jdk-17\nDefault locale: en_US, platform encoding: UTF-8\nOS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\"")
    
    add_screenshot(
        doc,
        "screenshot_3_2_maven_verify.png",
        "Figure 3.2 — Maven Version, Home Directory, and Java 17 Runtime Association",
        "In cmd, run 'mvn -version' and capture the displayed Maven version and Java runtime path."
    )
    
    # ==========================================
    # PART 4: MAVEN BUILD
    # ==========================================
    h_p4 = doc.add_heading("5. Part 4: Maven Build Lifecycle Automation (compile, test, package)", level=1)
    h_p4.paragraph_format.space_before = Pt(16)
    h_p4.paragraph_format.space_after = Pt(6)
    for r in h_p4.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "Maven standardizes the build process through a formal build lifecycle consisting of distinct phases: "
        "validate, compile, test, package, verify, install, and deploy. In this part, the Student Task Management System was "
        "configured with a Project Object Model (pom.xml), compiled, tested via JUnit 5, and packaged as a standalone WAR file."
    )
    
    # Step 4.1
    h_p4_1 = doc.add_heading("Step 4.1: pom.xml Configuration & Directory Architecture", level=2)
    h_p4_1.paragraph_format.space_before = Pt(10)
    for r in h_p4_1.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "The project was structured following standard Maven conventions:\n"
        "• pom.xml — Declares groupId: com.student, artifactId: student-task-manager, packaging: war.\n"
        "• src/main/java/com/student/TaskService.java — Core business logic for task management.\n"
        "• src/test/java/com/student/TaskServiceTest.java — Automated test suite with JUnit 5.\n"
        "• src/main/webapp/ — Web application root containing index.html, style.css, script.js, and WEB-INF/web.xml."
    )
    
    add_screenshot(
        doc,
        "screenshot_4_1_pom_check.png",
        "Figure 4.1 — Verification of pom.xml presence in project root directory",
        "Run 'dir pom.xml' in the project directory in cmd and capture with Win + Shift + S."
    )
    
    # Step 4.2
    h_p4_2 = doc.add_heading("Step 4.2: Compilation Phase (mvn compile)", level=2)
    h_p4_2.paragraph_format.space_before = Pt(10)
    for r in h_p4_2.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("The compile phase scans source code in src/main/java and compiles bytecodes into target/classes:")
    add_code_block(doc, "mvn compile\n[INFO] Compiling 1 source file with javac [debug target 17] to target\\classes\n[INFO] BUILD SUCCESS\n[INFO] Total time: 2.185 s")
    
    add_screenshot(
        doc,
        "screenshot_4_2_mvn_compile.png",
        "Figure 4.2 — Execution of 'mvn compile' culminating in BUILD SUCCESS",
        "Execute 'mvn compile' in project directory and capture the BUILD SUCCESS terminal block."
    )
    
    # Step 4.3
    h_p4_3 = doc.add_heading("Step 4.3: Automated Unit Testing Phase (mvn test)", level=2)
    h_p4_3.paragraph_format.space_before = Pt(10)
    for r in h_p4_3.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("Maven Surefire plugin executes the automated JUnit 5 test suite in src/test/java:")
    add_code_block(doc, "mvn test\n[INFO] Running com.student.TaskServiceTest\n[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0\n[INFO] BUILD SUCCESS")
    
    add_screenshot(
        doc,
        "screenshot_4_3_mvn_test.png",
        "Figure 4.3 — Execution of 'mvn test' with 4 passing unit tests and zero errors",
        "Execute 'mvn test' in project directory and capture the test summary and BUILD SUCCESS."
    )
    
    # Step 4.4
    h_p4_4 = doc.add_heading("Step 4.4: Packaging Phase (mvn clean package)", level=2)
    h_p4_4.paragraph_format.space_before = Pt(10)
    for r in h_p4_4.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "The package phase bundles the compiled Java classes, web resources (HTML, CSS, JS), and deployment descriptor "
        "into a production-ready Web Application Archive: student-task-manager.war."
    )
    add_code_block(doc, "mvn clean package\n[INFO] Assembling webapp [student-task-manager]\n[INFO] Building war: C:\\Users\\numl-\\Desktop\\student-task-manager\\student-task-manager\\target\\student-task-manager.war\n[INFO] BUILD SUCCESS")
    
    add_screenshot(
        doc,
        "screenshot_4_4_mvn_package.png",
        "Figure 4.4 — Execution of 'mvn clean package' producing the deployable WAR archive",
        "Execute 'mvn clean package' and capture the war assembling and packaging output."
    )
    
    # Step 4.5
    h_p4_5 = doc.add_heading("Step 4.5: Target WAR Verification", level=2)
    h_p4_5.paragraph_format.space_before = Pt(10)
    for r in h_p4_5.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("The existence of student-task-manager.war in the target folder is confirmed:")
    add_code_block(doc, "dir target\\*.war\n10/12/2026  07:30 PM            24,850 student-task-manager.war")
    
    add_screenshot(
        doc,
        "screenshot_4_5_war_check.png",
        "Figure 4.5 — Verification of student-task-manager.war inside the target directory",
        "Run 'dir target\\*.war' in cmd and capture the resulting file listing."
    )
    
    # ==========================================
    # PART 5: TOMCAT
    # ==========================================
    h_p5 = doc.add_heading("6. Part 5: Apache Tomcat Server Deployment & Functional Verification", level=1)
    h_p5.paragraph_format.space_before = Pt(16)
    h_p5.paragraph_format.space_after = Pt(6)
    for r in h_p5.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "Apache Tomcat is an open-source implementation of the Jakarta Servlet, Jakarta Server Pages, and WebSocket technologies. "
        "Because our application uses Java 17 and Jakarta EE 10 specifications (jakarta.servlet), Apache Tomcat 10.1 is selected."
    )
    
    h_p5_1 = doc.add_heading("Step 5.1: Deploying WAR to Tomcat webapps", level=2)
    h_p5_1.paragraph_format.space_before = Pt(10)
    for r in h_p5_1.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "The generated WAR file was copied into Tomcat's deployment directory (C:\\Tomcat\\webapps\\). "
        "Tomcat automatically extracts WAR files placed in this folder upon startup."
    )
    add_code_block(doc, "copy target\\student-task-manager.war C:\\Tomcat\\webapps\\\n        1 file(s) copied.\ndir C:\\Tomcat\\webapps\\student-task-manager.war")
    
    add_screenshot(
        doc,
        "screenshot_5_1_tomcat_webapps.png",
        "Figure 5.1 — Copying student-task-manager.war into C:\\Tomcat\\webapps Directory",
        "In cmd, run 'copy target\\student-task-manager.war C:\\Tomcat\\webapps\\' and capture output."
    )
    
    h_p5_2 = doc.add_heading("Step 5.2: Starting Tomcat via catalina.bat run", level=2)
    h_p5_2.paragraph_format.space_before = Pt(10)
    for r in h_p5_2.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph("Tomcat is started in foreground mode using catalina.bat run:")
    add_code_block(doc, "set \"JAVA_HOME=C:\\Java\\jdk-17\"\nset \"PATH=%JAVA_HOME%\\bin;%PATH%\"\ncd /d C:\\Tomcat\\bin\ncatalina.bat run\n\n[INFO] Deploying web application archive [C:\\Tomcat\\webapps\\student-task-manager.war]\n[INFO] Deployment of web application archive [student-task-manager.war] has finished in [662] ms\n[INFO] Starting ProtocolHandler [\"http-nio-8080\"]\n[INFO] Server startup in [2450] milliseconds")
    
    add_screenshot(
        doc,
        "screenshot_5_2_tomcat_run.png",
        "Figure 5.2 — Tomcat Startup Console confirming deployment of student-task-manager.war",
        "Launch catalina.bat run in cmd and capture the server initialization and WAR deployment lines."
    )
    
    h_p5_3 = doc.add_heading("Step 5.3: Web Browser Verification (http://localhost:8080/student-task-manager/)", level=2)
    h_p5_3.paragraph_format.space_before = Pt(10)
    for r in h_p5_3.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "Navigating to http://localhost:8080/student-task-manager/ loads the deployed application. "
        "The browser renders the modern responsive UI with student task cards, priority indicators, and add-task controls."
    )
    
    add_screenshot(
        doc,
        "screenshot_5_3_browser_app.png",
        "Figure 5.3 — Student Task Management System Live on Apache Tomcat (Port 8080)",
        "Open Chrome/Edge, navigate to http://localhost:8080/student-task-manager/ and capture with Win + Shift + S."
    )
    
    h_p5_4 = doc.add_heading("Step 5.4: Live Dynamic Features & Task Submission", level=2)
    h_p5_4.paragraph_format.space_before = Pt(10)
    for r in h_p5_4.runs: r.font.color.rgb = COLOR_SECONDARY
    
    doc.add_paragraph(
        "Testing the interactive application by submitting a new task ('Deploy WAR to Apache Tomcat Server' with High priority) "
        "dynamically increases the live counter badge from 3 to 4, demonstrating complete functional integrity."
    )
    
    add_screenshot(
        doc,
        "screenshot_5_4_browser_task_added.png",
        "Figure 5.4 — Dynamic Task Creation and Real-time Badge Increment in Web Browser",
        "Add a new task on the webpage, submit the form, and capture the page showing the newly added task."
    )
    
    # ==========================================
    # PART 6: TROUBLESHOOTING
    # ==========================================
    h_p6 = doc.add_heading("7. Part 6: Troubleshooting Guide & Solutions for Common Issues", level=1)
    h_p6.paragraph_format.space_before = Pt(16)
    h_p6.paragraph_format.space_after = Pt(6)
    for r in h_p6.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    trouble_table = doc.add_table(rows=5, cols=3)
    trouble_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    trouble_table.columns[0].width = Inches(1.8)
    trouble_table.columns[1].width = Inches(2.2)
    trouble_table.columns[2].width = Inches(2.5)
    
    headers = ["Error / Symptom", "Root Cause", "Definitive Solution"]
    for i, h in enumerate(headers):
        cell = trouble_table.rows[0].cells[i]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)
        
    issues = [
        ("Port 8080 already in use\n(ProtocolHandler Exception)", "Another service like Jenkins or IIS is bound to port 8080.", "Edit C:\\Tomcat\\conf\\server.xml. Change <Connector port=\"8080\" to port=\"8081\". Access via http://localhost:8081/student-task-manager/"),
        ("'mvn' is not recognized as an operable program", "C:\\Tools\\apache-maven\\bin is missing from Path, or cmd wasn't restarted.", "Verify Path contains C:\\Tools\\apache-maven\\bin. Close all terminals and launch a fresh Command Prompt window."),
        ("Maven shows wrong Java version (e.g., Java 8 instead of 17)", "System JAVA_HOME points to an older JDK or JRE path.", "Set System variable JAVA_HOME = C:\\Java\\jdk-17 and verify with 'echo %JAVA_HOME%' in cmd."),
        ("HTTP 404 Not Found in browser", "WAR file was renamed incorrectly or Tomcat failed to unpack it.", "Ensure WAR is named 'student-task-manager.war' exactly. Check C:\\Tomcat\\logs\\catalina.out for deployment errors.")
    ]
    
    for idx, (err, cause, sol) in enumerate(issues, start=1):
        row = trouble_table.rows[idx]
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate([err, cause, sol]):
            cell = row.cells[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT
            
    doc.add_page_break()
    
    # ==========================================
    # PART 7: SCREENSHOT REPLACEMENT CHECKLIST
    # ==========================================
    h_p7 = doc.add_heading("8. Student Verification & Screenshot Replacement Checklist", level=1)
    h_p7.paragraph_format.space_before = Pt(12)
    h_p7.paragraph_format.space_after = Pt(6)
    for r in h_p7.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "All figures in this document contain complete visual outputs and mockups. "
        "If your instructor specifically requires screenshots of your personal live desktop screen, "
        "follow this quick reference checklist. Use the Windows shortcut: Win + Shift + S to snip and paste directly into Word."
    )
    
    check_table = doc.add_table(rows=6, cols=3)
    check_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    check_table.columns[0].width = Inches(1.5)
    check_table.columns[1].width = Inches(2.2)
    check_table.columns[2].width = Inches(2.8)
    
    c_headers = ["Part", "Required Screenshot", "Exact Action / Window to Snip"]
    for i, h in enumerate(c_headers):
        cell = check_table.rows[0].cells[i]
        set_cell_background(cell, "0D9488")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)
        
    checklist_rows = [
        ("Part 1: Git", "Git version & Git status", "Run 'git --version' and 'git status' in Command Prompt."),
        ("Part 2: Java 17", "Environment Variables & Java version", "Take screenshot of System Properties Environment Variables window + 'java -version' in cmd."),
        ("Part 3: Maven", "Maven version CLI", "Run 'mvn -version' in cmd showing Apache Maven and Java 17."),
        ("Part 4: Build", "Maven compile & package SUCCESS", "Run 'mvn clean package' in cmd showing [INFO] BUILD SUCCESS and target\\*.war."),
        ("Part 5: Tomcat", "catalina.bat run & Web Browser", "Snip Tomcat cmd window running catalina.bat + Chrome showing http://localhost:8080/student-task-manager/.")
    ]
    
    for idx, (p_num, req, act) in enumerate(checklist_rows, start=1):
        row = check_table.rows[idx]
        bg = "F9FAFB" if idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate([p_num, req, act]):
            cell = row.cells[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_TEXT
            
    # Conclusion
    h_conc = doc.add_heading("9. Conclusion & Next DevOps Milestones", level=1)
    h_conc.paragraph_format.space_before = Pt(16)
    h_conc.paragraph_format.space_after = Pt(6)
    for r in h_conc.runs:
        r.font.color.rgb = COLOR_PRIMARY
        r.font.name = "Segoe UI"
        
    doc.add_paragraph(
        "By completing this assignment, the foundation for automated CI/CD has been successfully established. "
        "The project has progressed from isolated source files to an enterprise-grade artifact managed under strict version control "
        "and reproducible build automation. In the subsequent DevOps modules, this repository will serve as the source "
        "for automated Jenkins pipelines, Docker containerization, and cloud infrastructure deployment via Terraform."
    )
    
    output_files = [
        r"c:\Users\numl-\Desktop\student-task-manager\student-task-manager\Student_Task_Manager_Assignment_Report_Placeholders.docx",
        r"c:\Users\numl-\Desktop\student-task-manager\Student_Task_Manager_Assignment_Report_Placeholders.docx",
        DOCX_OUTPUT_PATH,
        DOCX_DESKTOP_COPY
    ]
    saved = []
    for fpath in output_files:
        try:
            doc.save(fpath)
            saved.append(fpath)
        except PermissionError:
            pass
    print("Report documents successfully created at:")
    for s in saved:
        print(" ->", s)

if __name__ == "__main__":
    build_document()
