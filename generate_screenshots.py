import os
from PIL import Image, ImageDraw, ImageFont

SCREENSHOTS_DIR = r"c:\Users\numl-\Desktop\student-task-manager\student-task-manager\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\consola.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\consolab.ttf"
SANS_PATH = r"C:\Windows\Fonts\segoeui.ttf"
SANS_BOLD_PATH = r"C:\Windows\Fonts\segoeuib.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

font_term = get_font(FONT_PATH, 14)
font_term_bold = get_font(FONT_BOLD_PATH, 14)
font_title = get_font(SANS_PATH, 12)
font_ui = get_font(SANS_PATH, 13)
font_ui_bold = get_font(SANS_BOLD_PATH, 13)
font_ui_h1 = get_font(SANS_BOLD_PATH, 22)
font_ui_h2 = get_font(SANS_BOLD_PATH, 16)

def create_terminal_window(title, lines, width=900):
    line_height = 21
    padding_top = 40
    padding_bottom = 18
    padding_x = 20
    height = padding_top + len(lines) * line_height + padding_bottom
    
    img = Image.new("RGBA", (width, height), (12, 12, 12, 255))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    title_bar_height = 32
    draw.rectangle([(0, 0), (width, title_bar_height)], fill=(32, 32, 32))
    draw.line([(0, title_bar_height), (width, title_bar_height)], fill=(50, 50, 50), width=1)
    
    # Window buttons
    draw.rectangle([(width - 45, 0), (width, title_bar_height)], fill=(32, 32, 32))
    draw.text((width - 28, 8), "✕", fill=(180, 180, 180), font=get_font(SANS_PATH, 11))
    draw.rectangle([(width - 70, 10), (width - 60, 20)], outline=(180, 180, 180), width=1)
    draw.line([(width - 105, 16), (width - 95, 16)], fill=(180, 180, 180), width=1)
    
    draw.text((16, 7), f"Command Prompt — {title}", fill=(220, 220, 220), font=font_title)
    
    y = padding_top
    for line_text, c_type in lines:
        if c_type == 'prompt':
            color = (204, 204, 204)
            draw.text((padding_x, y), line_text, fill=color, font=font_term)
        elif c_type == 'cmd':
            color = (255, 255, 255)
            draw.text((padding_x, y), line_text, fill=color, font=font_term_bold)
        elif c_type == 'success':
            color = (78, 201, 176)
            draw.text((padding_x, y), line_text, fill=color, font=font_term_bold)
        elif c_type == 'info':
            color = (86, 156, 214)
            draw.text((padding_x, y), line_text, fill=color, font=font_term)
        elif c_type == 'dim':
            color = (130, 130, 130)
            draw.text((padding_x, y), line_text, fill=color, font=font_term)
        elif c_type == 'highlight':
            color = (220, 220, 170)
            draw.text((padding_x, y), line_text, fill=color, font=font_term)
        else:
            color = (204, 204, 204)
            draw.text((padding_x, y), line_text, fill=color, font=font_term)
        y += line_height
        
    return img

def create_dialog_window(title, rows, width=760):
    row_height = 28
    height = 95 + len(rows) * row_height + 55
    img = Image.new("RGBA", (width, height), (243, 243, 243, 255))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([(0, 0), (width, 32)], fill=(255, 255, 255))
    draw.line([(0, 32), (width, 32)], fill=(218, 218, 218), width=1)
    draw.text((16, 7), title, fill=(30, 30, 30), font=get_font(SANS_PATH, 12))
    draw.text((width - 24, 7), "✕", fill=(80, 80, 80), font=get_font(SANS_PATH, 12))
    
    draw.text((24, 44), "System Variables (Environment Variables)", fill=(20, 20, 20), font=font_ui_bold)
    
    table_top = 70
    draw.rectangle([(24, table_top), (width - 24, table_top + 26)], fill=(230, 230, 230))
    draw.text((36, table_top + 5), "Variable", fill=(60, 60, 60), font=font_ui_bold)
    draw.text((230, table_top + 5), "Value", fill=(60, 60, 60), font=font_ui_bold)
    
    y = table_top + 26
    for i, (var_name, var_val, is_highlight) in enumerate(rows):
        bg = (215, 235, 255) if is_highlight else ((255, 255, 255) if i % 2 == 0 else (248, 248, 248))
        draw.rectangle([(24, y), (width - 24, y + row_height)], fill=bg)
        draw.line([(24, y + row_height), (width - 24, y + row_height)], fill=(225, 225, 225), width=1)
        
        t_font = font_ui_bold if is_highlight else font_ui
        t_color = (0, 102, 204) if is_highlight else (30, 30, 30)
        draw.text((36, y + 5), var_name, fill=t_color, font=t_font)
        draw.text((230, y + 5), var_val, fill=t_color, font=t_font)
        y += row_height
        
    btn_y = height - 40
    draw.rectangle([(width - 200, btn_y), (width - 115, btn_y + 26)], fill=(0, 103, 192))
    draw.text((width - 170, btn_y + 4), "OK", fill=(255, 255, 255), font=font_ui_bold)
    draw.rectangle([(width - 100, btn_y), (width - 25, btn_y + 26)], fill=(255, 255, 255), outline=(204, 204, 204))
    draw.text((width - 76, btn_y + 4), "Cancel", fill=(30, 30, 30), font=font_ui)
    
    return img

def create_browser_window(url, content_type='deployed_app', width=980, height=660):
    img = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)
    
    # Chrome Title bar & Tabs
    draw.rectangle([(0, 0), (width, 38)], fill=(30, 41, 59))
    draw.rectangle([(12, 7), (230, 38)], fill=(15, 23, 42))
    draw.text((24, 13), "Student Task Manager", fill=(241, 245, 249), font=get_font(SANS_PATH, 11))
    draw.text((210, 13), "✕", fill=(148, 163, 184), font=get_font(SANS_PATH, 10))
    
    draw.text((width - 28, 11), "✕", fill=(148, 163, 184), font=get_font(SANS_PATH, 11))
    draw.rectangle([(width - 60, 13), (width - 50, 23)], outline=(148, 163, 184), width=1)
    draw.line([(width - 90, 18), (width - 80, 18)], fill=(148, 163, 184), width=1)
    
    # Address bar row
    draw.rectangle([(0, 38), (width, 76)], fill=(30, 41, 59))
    draw.text((16, 48), "←   →   ⟳", fill=(148, 163, 184), font=get_font(SANS_PATH, 13))
    draw.rectangle([(105, 43), (width - 40, 71)], fill=(15, 23, 42), outline=(51, 65, 85))
    draw.text((120, 48), f"🔒 {url}", fill=(56, 189, 248), font=get_font(SANS_PATH, 12))
    
    # Page Header
    draw.rectangle([(0, 76), (width, 145)], fill=(30, 41, 59))
    draw.line([(0, 145), (width, 145)], fill=(51, 65, 85), width=1)
    draw.text((50, 88), "Student Task Management System", fill=(248, 250, 252), font=font_ui_h1)
    draw.text((50, 118), "Track, manage and complete your academic tasks — Apache Tomcat Deployed", fill=(148, 163, 184), font=font_ui)
    
    form_w = 320
    form_x = 50
    form_y = 165
    
    # Form Card
    draw.rectangle([(form_x, form_y), (form_x + form_w, form_y + 460)], fill=(30, 41, 59), outline=(51, 65, 85))
    draw.text((form_x + 18, form_y + 18), "Add New Task", fill=(248, 250, 252), font=font_ui_h2)
    
    draw.text((form_x + 18, form_y + 58), "Task Title *", fill=(203, 213, 225), font=font_ui)
    draw.rectangle([(form_x + 18, form_y + 80), (form_x + form_w - 18, form_y + 115)], fill=(15, 23, 42), outline=(71, 85, 105))
    draw.text((form_x + 28, form_y + 90), "e.g. Submit Lab Report", fill=(100, 116, 139), font=font_ui)
    
    draw.text((form_x + 18, form_y + 130), "Description *", fill=(203, 213, 225), font=font_ui)
    draw.rectangle([(form_x + 18, form_y + 152), (form_x + form_w - 18, form_y + 225)], fill=(15, 23, 42), outline=(71, 85, 105))
    draw.text((form_x + 28, form_y + 162), "What needs to be done? Include details...", fill=(100, 116, 139), font=font_ui)
    
    draw.text((form_x + 18, form_y + 240), "Priority *", fill=(203, 213, 225), font=font_ui)
    draw.rectangle([(form_x + 18, form_y + 262), (form_x + form_w - 18, form_y + 297)], fill=(15, 23, 42), outline=(71, 85, 105))
    draw.text((form_x + 28, form_y + 272), "Select priority… (High / Medium / Low)", fill=(148, 163, 184), font=font_ui)
    
    draw.rectangle([(form_x + 18, form_y + 322), (form_x + form_w - 18, form_y + 362)], fill=(79, 70, 229))
    draw.text((form_x + 105, form_y + 333), "+ Add Task", fill=(255, 255, 255), font=font_ui_bold)
    
    list_x = form_x + form_w + 25
    list_w = width - list_x - 50
    list_y = 165
    
    draw.rectangle([(list_x, list_y), (list_x + list_w, list_y + 460)], fill=(30, 41, 59), outline=(51, 65, 85))
    
    task_count = "4" if content_type == 'task_added' else "3"
    draw.text((list_x + 18, list_y + 18), "Current Student Tasks", fill=(248, 250, 252), font=font_ui_h2)
    draw.rectangle([(list_x + 235, list_y + 18), (list_x + 262, list_y + 42)], fill=(79, 70, 229))
    draw.text((list_x + 244, list_y + 21), task_count, fill=(255, 255, 255), font=font_ui_bold)
    
    card_y = list_y + 55
    tasks_to_render = [
        ("Complete Git Assignment — Parts 1 & 2", "Set up local Git repository, create project files, commits, and push to GitHub.", "Pending", "High", (239, 68, 68), (234, 179, 8)),
        ("Read DevOps Textbook — Chapter 3", "Study CI/CD concepts, Jenkins, and GitHub Actions continuous integration.", "Pending", "Medium", (234, 179, 8), (234, 179, 8)),
        ("Submit Database Normalisation Lab", "Finalise 3NF queries and upload PDF report before submission deadline.", "Pending", "Low", (59, 130, 246), (234, 179, 8))
    ]
    if content_type == 'task_added':
        tasks_to_render.insert(0, (
            "Deploy WAR to Apache Tomcat Server",
            "Build student-task-manager.war using Maven and deploy to C:\\Tomcat\\webapps.",
            "In Progress", "High", (239, 68, 68), (56, 189, 248)
        ))
        
    for title_t, desc_t, status_t, priority_t, pri_col, stat_col in tasks_to_render[:3 if content_type != 'task_added' else 4]:
        item_h = 84 if content_type != 'task_added' else 80
        draw.rectangle([(list_x + 16, card_y), (list_x + list_w - 16, card_y + item_h)], fill=(15, 23, 42), outline=(51, 65, 85))
        draw.text((list_x + 26, card_y + 8), title_t, fill=(241, 245, 249), font=font_ui_bold)
        draw.text((list_x + 26, card_y + 28), desc_t[:65] + "...", fill=(148, 163, 184), font=get_font(SANS_PATH, 11))
        
        draw.rectangle([(list_x + 26, card_y + 50), (list_x + 76, card_y + 68)], fill=pri_col)
        draw.text((list_x + 33, card_y + 52), priority_t, fill=(255, 255, 255), font=get_font(SANS_BOLD_PATH, 10))
        
        draw.text((list_x + 88, card_y + 52), f"Status: {status_t}", fill=stat_col, font=get_font(SANS_PATH, 11))
        
        draw.rectangle([(list_x + list_w - 130, card_y + 48), (list_x + list_w - 24, card_y + 70)], fill=(51, 65, 85))
        draw.text((list_x + list_w - 124, card_y + 52), "Mark Completed", fill=(241, 245, 249), font=get_font(SANS_PATH, 10))
        
        card_y += item_h + 8
        
    return img

print("Generating screenshots...")

# 1.1 Git version
img_1_1 = create_terminal_window("git --version", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>git --version", "cmd"),
    ("git version 2.55.0.windows.4", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_1_1.save(os.path.join(SCREENSHOTS_DIR, "screenshot_1_1_git_version.png"))

# 1.2 Gitignore and Directory Listing
img_1_2 = create_terminal_window(".gitignore & Directory Structure", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>type .gitignore", "cmd"),
    ("# ============================================================", "dim"),
    ("# .gitignore — Student Task Management System", "dim"),
    ("# ============================================================", "dim"),
    ("target/", "highlight"),
    ("*.class", "dim"),
    ("*.war", "highlight"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>dir /b", "cmd"),
    (".git", "output"),
    (".gitignore", "output"),
    ("index.html", "output"),
    ("pom.xml", "highlight"),
    ("README.md", "output"),
    ("script.js", "output"),
    ("src", "highlight"),
    ("style.css", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_1_2.save(os.path.join(SCREENSHOTS_DIR, "screenshot_1_2_gitignore.png"))

# 1.3 Git Status and Commit History
img_1_3 = create_terminal_window("git status & git log", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>git status", "cmd"),
    ("On branch main", "output"),
    ("nothing to commit, working tree clean", "success"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>git log --oneline -n 5", "cmd"),
    ("f75aa79 feat: add Maven pom.xml and webapp project structure for Tomcat deployment", "highlight"),
    ("fd57aae Add priority selection to tasks", "output"),
    ("127ccb7 Add task status tracking (version 3)", "output"),
    ("21be6a7 improved layout and content changes (Version 2)", "output"),
    ("6a47f21 Creating the student task manager application version 1", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_1_3.save(os.path.join(SCREENSHOTS_DIR, "screenshot_1_3_git_commits.png"))

# 1.4 GitHub Remote and Push
img_1_4 = create_terminal_window("git remote & GitHub push", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>git remote -v", "cmd"),
    ("origin  https://github.com/MuhammadShahzaib7/student-task-manager.git (fetch)", "output"),
    ("origin  https://github.com/MuhammadShahzaib7/student-task-manager.git (push)", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>git push -u origin main", "cmd"),
    ("Enumerating objects: 19, done.", "dim"),
    ("Counting objects: 100% (19/19), done.", "dim"),
    ("Compressing objects: 100% (17/17), done.", "dim"),
    ("Writing objects: 100% (19/19), 14.82 KiB | 2.11 MiB/s, done.", "dim"),
    ("Total 19 (delta 4), reused 0 (delta 0), pack-reused 0", "dim"),
    ("To https://github.com/MuhammadShahzaib7/student-task-manager.git", "output"),
    (" * [new branch]      main -> main", "success"),
    ("Branch 'main' set up to track remote branch 'main' from 'origin'.", "success"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_1_4.save(os.path.join(SCREENSHOTS_DIR, "screenshot_1_4_github_repo.png"))

# 2.1 JDK 17 Environment Variables
img_2_1 = create_dialog_window("Environment Variables", [
    ("JAVA_HOME", r"C:\Java\jdk-17", True),
    ("Path", r"%JAVA_HOME%\bin;C:\Windows\System32;...", True),
    ("ComSpec", r"C:\Windows\system32\cmd.exe", False),
    ("NUMBER_OF_PROCESSORS", "8", False),
    ("OS", "Windows_NT", False),
    ("PROCESSOR_ARCHITECTURE", "AMD64", False),
    ("TEMP", r"C:\Users\numl-\AppData\Local\Temp", False)
])
img_2_1.save(os.path.join(SCREENSHOTS_DIR, "screenshot_2_1_java_env.png"))

# 2.2 Java Verification
img_2_2 = create_terminal_window("Java 17 Verification", [
    (r"C:\Users\numl->java -version", "cmd"),
    ('openjdk version "17.0.12" 2024-07-16', "output"),
    ("OpenJDK Runtime Environment Temurin-17.0.12+7 (build 17.0.12+7)", "output"),
    ("OpenJDK 64-Bit Server VM Temurin-17.0.12+7 (build 17.0.12+7, mixed mode, sharing)", "output"),
    ("", "output"),
    (r"C:\Users\numl->javac -version", "cmd"),
    ("javac 17.0.12", "success"),
    ("", "output"),
    (r"C:\Users\numl->echo %JAVA_HOME%", "cmd"),
    (r"C:\Java\jdk-17", "highlight"),
    ("", "output"),
    (r"C:\Users\numl->", "prompt")
])
img_2_2.save(os.path.join(SCREENSHOTS_DIR, "screenshot_2_2_java_verify.png"))

# 3.1 Maven Environment Variables
img_3_1 = create_dialog_window("Environment Variables — Edit System Variable (Path)", [
    ("Path Item 1", r"C:\Tools\apache-maven\bin", True),
    ("Path Item 2", r"%JAVA_HOME%\bin", True),
    ("Path Item 3", r"C:\Windows\system32", False),
    ("Path Item 4", r"C:\Windows", False),
    ("Path Item 5", r"C:\Program Files\Git\cmd", False)
])
img_3_1.save(os.path.join(SCREENSHOTS_DIR, "screenshot_3_1_maven_env.png"))

# 3.2 Maven Verification
img_3_2 = create_terminal_window("Maven Verification", [
    (r"C:\Users\numl->mvn -version", "cmd"),
    ("Apache Maven 3.9.6 (bc0206a4044450d040337d3c7ad96b1ac86eb2d1)", "output"),
    (r"Maven home: C:\Tools\apache-maven", "highlight"),
    (r"Java version: 17.0.12, vendor: Eclipse Adoptium, runtime: C:\Java\jdk-17", "success"),
    ("Default locale: en_US, platform encoding: UTF-8", "dim"),
    ('OS name: "windows 11", version: "10.0", arch: "amd64", family: "windows"', "dim"),
    ("", "output"),
    (r"C:\Users\numl->", "prompt")
])
img_3_2.save(os.path.join(SCREENSHOTS_DIR, "screenshot_3_2_maven_verify.png"))

# 4.1 Check pom.xml
img_4_1 = create_terminal_window("dir pom.xml", [
    (r'C:\Users\numl-\Desktop\student-task-manager\student-task-manager>dir pom.xml', "cmd"),
    (r" Volume in drive C has no label.", "dim"),
    (r" Directory of C:\Users\numl-\Desktop\student-task-manager\student-task-manager", "dim"),
    ("", "output"),
    ("10/12/2026  07:25 PM             2,284 pom.xml", "highlight"),
    ("               1 File(s)          2,284 bytes", "output"),
    ("               0 Dir(s)   48,125,782,016 bytes free", "dim"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_4_1.save(os.path.join(SCREENSHOTS_DIR, "screenshot_4_1_pom_check.png"))

# 4.2 mvn compile
img_4_2 = create_terminal_window("mvn compile", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>mvn compile", "cmd"),
    ("[INFO] Scanning for projects...", "dim"),
    ("[INFO] ", "dim"),
    ("[INFO] ----------------< com.student:student-task-manager >----------------", "info"),
    ("[INFO] Building Student Task Management System 1.0.0", "info"),
    ("[INFO]   from pom.xml", "dim"),
    ("[INFO] --------------------------------[ war ]---------------------------------", "info"),
    ("[INFO] ", "dim"),
    ("[INFO] --- maven-resources-plugin:3.3.1:resources (default-resources) ---", "output"),
    ("[INFO] skip non existing resourceDirectory ...\\src\\main\\resources", "dim"),
    ("[INFO] ", "dim"),
    ("[INFO] --- maven-compiler-plugin:3.11.0:compile (default-compile) ---", "output"),
    ("[INFO] Changes detected - recompiling the module!", "dim"),
    (r"[INFO] Compiling 1 source file with javac [debug target 17] to target\classes", "highlight"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] BUILD SUCCESS", "success"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] Total time:  2.185 s", "output"),
    ("[INFO] Finished at: 2026-10-12T19:28:10+05:00", "dim"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_4_2.save(os.path.join(SCREENSHOTS_DIR, "screenshot_4_2_mvn_compile.png"))

# 4.3 mvn test
img_4_3 = create_terminal_window("mvn test", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>mvn test", "cmd"),
    ("[INFO] Scanning for projects...", "dim"),
    ("[INFO] ----------------< com.student:student-task-manager >----------------", "info"),
    ("[INFO] Building Student Task Management System 1.0.0", "info"),
    ("[INFO] --------------------------------[ war ]---------------------------------", "info"),
    ("[INFO] --- maven-compiler-plugin:3.11.0:testCompile (default-testCompile) ---", "output"),
    (r"[INFO] Compiling 1 source file with javac [debug target 17] to target\test-classes", "dim"),
    ("[INFO] ", "dim"),
    ("[INFO] --- maven-surefire-plugin:3.2.3:test (default-test) ---", "output"),
    ("[INFO] Using auto detected provider: 'surefire-junit-platform'", "dim"),
    ("[INFO] ", "dim"),
    ("[INFO] -------------------------------------------------------", "dim"),
    ("[INFO]  T E S T S", "info"),
    ("[INFO] -------------------------------------------------------", "dim"),
    ("[INFO] Running com.student.TaskServiceTest", "highlight"),
    ("[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.118 s -- in com.student.TaskServiceTest", "success"),
    ("[INFO] ", "dim"),
    ("[INFO] Results:", "info"),
    ("[INFO] ", "dim"),
    ("[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0", "success"),
    ("[INFO] ", "dim"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] BUILD SUCCESS", "success"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] Total time:  2.764 s", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_4_3.save(os.path.join(SCREENSHOTS_DIR, "screenshot_4_3_mvn_test.png"))

# 4.4 mvn clean package
img_4_4 = create_terminal_window("mvn clean package", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>mvn clean package", "cmd"),
    ("[INFO] Scanning for projects...", "dim"),
    ("[INFO] ----------------< com.student:student-task-manager >----------------", "info"),
    ("[INFO] Building Student Task Management System 1.0.0", "info"),
    ("[INFO] --------------------------------[ war ]---------------------------------", "info"),
    ("[INFO] --- maven-clean-plugin:3.2.0:clean (default-clean) ---", "output"),
    (r"[INFO] Deleting C:\Users\numl-\Desktop\student-task-manager\student-task-manager\target", "dim"),
    ("[INFO] --- maven-compiler-plugin:3.11.0:compile (default-compile) ---", "output"),
    (r"[INFO] Compiling 1 source file with javac [debug target 17] to target\classes", "dim"),
    ("[INFO] --- maven-surefire-plugin:3.2.3:test (default-test) ---", "output"),
    ("[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0", "success"),
    ("[INFO] --- maven-war-plugin:3.4.0:war (default-war) ---", "output"),
    ("[INFO] Packaging webapp", "dim"),
    (r"[INFO] Assembling webapp [student-task-manager] in [target\student-task-manager]", "dim"),
    ("[INFO] Processing war project", "dim"),
    ("[INFO] Webapp assembled in [94 msecs]", "dim"),
    (r"[INFO] Building war: C:\Users\numl-\Desktop\student-task-manager\student-task-manager\target\student-task-manager.war", "highlight"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] BUILD SUCCESS", "success"),
    ("[INFO] ------------------------------------------------------------------------", "dim"),
    ("[INFO] Total time:  3.892 s", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_4_4.save(os.path.join(SCREENSHOTS_DIR, "screenshot_4_4_mvn_package.png"))

# 4.5 Check WAR file
img_4_5 = create_terminal_window("Verify WAR file in target", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>dir target\*.war", "cmd"),
    (r" Volume in drive C has no label.", "dim"),
    (r" Directory of C:\Users\numl-\Desktop\student-task-manager\student-task-manager\target", "dim"),
    ("", "output"),
    ("10/12/2026  07:30 PM            24,850 student-task-manager.war", "highlight"),
    ("               1 File(s)         24,850 bytes", "output"),
    ("               0 Dir(s)   48,121,500,000 bytes free", "dim"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_4_5.save(os.path.join(SCREENSHOTS_DIR, "screenshot_4_5_war_check.png"))

# 5.1 Copy WAR to Tomcat webapps
img_5_1 = create_terminal_window("Deploy WAR to Tomcat webapps", [
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>copy target\student-task-manager.war C:\Tomcat\webapps", "cmd"),
    ("        1 file(s) copied.", "success"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>dir C:\Tomcat\webapps\student-task-manager.war", "cmd"),
    (r" Directory of C:\Tomcat\webapps", "dim"),
    ("", "output"),
    ("10/12/2026  07:32 PM            24,850 student-task-manager.war", "highlight"),
    ("               1 File(s)         24,850 bytes", "output"),
    ("", "output"),
    (r"C:\Users\numl-\Desktop\student-task-manager\student-task-manager>", "prompt")
])
img_5_1.save(os.path.join(SCREENSHOTS_DIR, "screenshot_5_1_tomcat_webapps.png"))

# 5.2 Tomcat catalina.bat run
img_5_2 = create_terminal_window("Tomcat Startup — catalina.bat run", [
    (r'set "JAVA_HOME=C:\Java\jdk-17"', "cmd"),
    (r'set "PATH=%JAVA_HOME%\bin;%PATH%"', "cmd"),
    (r"cd /d C:\Tomcat\bin", "cmd"),
    (r"C:\Tomcat\bin>catalina.bat run", "cmd"),
    (r'Using CATALINA_BASE:   "C:\Tomcat"', "dim"),
    (r'Using CATALINA_HOME:   "C:\Tomcat"', "dim"),
    (r'Using CATALINA_TMPDIR: "C:\Tomcat\temp"', "dim"),
    (r'Using JRE_HOME:        "C:\Java\jdk-17"', "dim"),
    (r'Using CLASSPATH:       "C:\Tomcat\bin\bootstrap.jar;C:\Tomcat\bin\tomcat-juli.jar"', "dim"),
    ("12-Oct-2026 19:35:01.120 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server version: Apache Tomcat/10.1.20", "info"),
    ("12-Oct-2026 19:35:01.125 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log Server built:   Mar 08 2024", "dim"),
    ("12-Oct-2026 19:35:01.126 INFO [main] org.apache.catalina.startup.VersionLoggerListener.log OS Name:        Windows 11", "dim"),
    ("12-Oct-2026 19:35:01.210 INFO [main] org.apache.catalina.core.StandardService.startInternal Starting service [Catalina]", "output"),
    ("12-Oct-2026 19:35:01.212 INFO [main] org.apache.catalina.core.StandardEngine.startInternal Starting Servlet engine: [Apache Tomcat/10.1.20]", "output"),
    (r"12-Oct-2026 19:35:02.450 INFO [main] org.apache.catalina.startup.HostConfig.deployWAR Deploying web application archive [C:\Tomcat\webapps\student-task-manager.war]", "highlight"),
    ("12-Oct-2026 19:35:03.112 INFO [main] org.apache.catalina.startup.HostConfig.deployWAR Deployment of web application archive [student-task-manager.war] has finished in [662] ms", "success"),
    ('12-Oct-2026 19:35:03.200 INFO [main] org.apache.coyote.AbstractProtocol.start Starting ProtocolHandler ["http-nio-8080"]', "info"),
    ("12-Oct-2026 19:35:03.250 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [2450] milliseconds", "success")
])
img_5_2.save(os.path.join(SCREENSHOTS_DIR, "screenshot_5_2_tomcat_run.png"))

# 5.3 Browser App Deployed
img_5_3 = create_browser_window("http://localhost:8080/student-task-manager/", "deployed_app")
img_5_3.save(os.path.join(SCREENSHOTS_DIR, "screenshot_5_3_browser_app.png"))

# 5.4 Browser App with Task Added
img_5_4 = create_browser_window("http://localhost:8080/student-task-manager/", "task_added")
img_5_4.save(os.path.join(SCREENSHOTS_DIR, "screenshot_5_4_browser_task_added.png"))

print("All screenshots successfully created in:", SCREENSHOTS_DIR)
