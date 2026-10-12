# Student Task Management System — DevOps Assignment Report

**Project:** Student Task Management System (`student-task-manager`)  
**Course:** DevOps Practical Series & Continuous Integration  
**Student Name:** Noor Akhtar  
**Submission Date:** October 12, 2026  
**Repository:** [https://github.com/Noor1675/student-task-manager.git](https://github.com/Noor1675/student-task-manager.git)  

---

## 📌 Executive Summary

Yeh report DevOps Practical Assignment ke tamam 5 marahal (Part 1 se Part 5) ko step-by-step cover karti hai:
1. **Part 1:** Git version control setup, `.gitignore` configuration, staging, commits, aur GitHub remote configuration.
2. **Part 2:** Java Development Kit 17 (JDK 17 LTS) installation, `JAVA_HOME` aur System `Path` environment variables setup, aur CLI verification (`java -version`, `javac -version`).
3. **Part 3:** Apache Maven 3.9 installation, `Path` mein add karna, aur CLI verification (`mvn -version`).
4. **Part 4:** Maven `pom.xml` configuration, project architecture (`src/main/java`, `src/main/webapp`, `src/test/java`), automated testing (`mvn test`), aur WAR package generation (`mvn clean package` -> `target/student-task-manager.war`).
5. **Part 5:** Apache Tomcat 10.1 setup, `student-task-manager.war` ko `webapps` folder mein copy karna, Tomcat start karna (`catalina.bat run`), aur browser mein `http://localhost:8080/student-task-manager/` par live test karna.

> 📄 **MS Word Document (Placeholders File Ready):**  
> Complete Word Document report file with clean placeholder boxes yahan mojood hai:  
> **`Student_Task_Manager_Assignment_Report_Placeholders.docx`**  
> *(Aap is Word file ko open karke har placeholder box mein apna asli screenshot `Ctrl + V` se paste kar sakte hain!)*

---

## Part 1: Git Install aur GitHub par Code Daalna

### 1.1 Git Version Check
Terminal mein Git version verify karein:
```cmd
C:\Users\numl-\Desktop\student-task-manager\student-task-manager> git --version
git version 2.55.0.windows.4
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 1.1: Git Version Verification]**  
> **Command:** `git --version`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** Command aur uska output `git version 2.55.0.windows.4`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein placeholder par click karke `Ctrl + V` karein.

---

### 1.2 `.gitignore` File Configuration
Build outputs aur generated files (`target/`, `*.class`, `*.war`) ko Git repository se exclude karne ke liye `.gitignore` configure kiya gaya:
```gitignore
# Maven Build Output
target/
*.class
*.war
```

```cmd
C:\Users\numl-\Desktop\student-task-manager\student-task-manager> type .gitignore
C:\Users\numl-\Desktop\student-task-manager\student-task-manager> dir /b
.git
.gitignore
index.html
pom.xml
README.md
script.js
src
style.css
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 1.2: .gitignore aur Project Files]**  
> **Command:** `type .gitignore` aur `dir /b`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** `.gitignore` ke andar `target/` aur project files ki list.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 1.3 Staging, Commits aur Git Status
Tamam files stage ki gayin aur meaningful commit messages ke sath commit ki gayin:
```cmd
git status
# On branch main
# nothing to commit, working tree clean

git log --oneline -n 5
f75aa79 feat: add Maven pom.xml and webapp project structure for Tomcat deployment
fd57aae Add priority selection to tasks
127ccb7 Add task status tracking (version 3)
21be6a7 improved layout and content changes (Version 2)
6a47f21 Creating the student task manager application version 1
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 1.3: Git Status aur Commits Log]**  
> **Command:** `git status` aur `git log --oneline -n 5`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** Clean working tree aur commits ki list (`feat: add Maven pom.xml...`).  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 1.4 GitHub Remote Push
GitHub par repository banakar remote set kiya gaya aur push synchronize kiya gaya:
```cmd
git remote set-url origin https://github.com/Noor1675/student-task-manager.git
git remote -v
origin  https://github.com/Noor1675/student-task-manager.git (fetch)
origin  https://github.com/Noor1675/student-task-manager.git (push)

git push -u origin main
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 1.4: GitHub Repository Webpage]**  
> **URL:** `https://github.com/Noor1675/student-task-manager`  
> **Window:** Browser (Chrome / Edge)  
> **Kya capture karna hai:** GitHub page jahan repository ka naam `Noor1675/student-task-manager`, files list (`pom.xml`, `src`, `index.html`), aur commit status nazar aaye.  
> **Shortcuts:** Browser mein page khol kar `Win + Shift + S` se screenshot lein -> Word mein paste karein.

---

## Part 2: JDK 17 Install aur Environment Variables Setup

### 2.1 Environment Variables Configuration
1. JDK 17 ko `C:\Java\jdk-17` mein install karein (ya jahan aapka JDK 17 install ho).
2. Windows System Environment Variables mein:
   - **Variable Name:** `JAVA_HOME`
   - **Variable Value:** `C:\Java\jdk-17`
3. System `Path` variable mein add karein:
   - `%JAVA_HOME%\bin`

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 2.1: System Environment Variables Dialog]**  
> **Window:** System Properties -> Environment Variables  
> **Kese kholna hai:** Start menu mein search karein "Edit the system environment variables" -> "Environment Variables" button par click karein.  
> **Kya capture karna hai:** System Variables table jahan `JAVA_HOME` (`C:\Java\jdk-17`) aur `Path` highlighted ho.  
> **Shortcuts:** `Win + Shift + S` se dialog box capture karein -> Word mein paste karein.

---

### 2.2 Java Runtime & Compiler Verification
Naye Command Prompt window mein Java aur Javac verify karein:
```cmd
C:\Users\numl-> java -version
openjdk version "17.0.12" 2024-07-16
OpenJDK Runtime Environment Temurin-17.0.12+7 (build 17.0.12+7)
OpenJDK 64-Bit Server VM Temurin-17.0.12+7 (build 17.0.12+7, mixed mode, sharing)

C:\Users\numl-> javac -version
javac 17.0.12

C:\Users\numl-> echo %JAVA_HOME%
C:\Java\jdk-17
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 2.2: java aur javac Verification]**  
> **Command:** `java -version`, `javac -version`, aur `echo %JAVA_HOME%`  
> **Window:** Naya Command Prompt  
> **Kya capture karna hai:** Output mein Java 17 ka version aur `JAVA_HOME` path.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

## Part 3: Maven Install aur Path Configuration

### 3.1 Apache Maven Setup
1. Apache Maven binary zip `maven.apache.org` se download karke `C:\Tools\apache-maven` mein extract karein.
2. System `Path` variable mein ye path add karein:
   - `C:\Tools\apache-maven\bin`

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 3.1: Maven Path in Environment Variables]**  
> **Window:** Edit Environment Variable (Path)  
> **Kese kholna hai:** Environment Variables -> System variables mein `Path` select karke `Edit` dabayein.  
> **Kya capture karna hai:** List jahan `C:\Tools\apache-maven\bin` line nazar aa rahi ho.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 3.2 Maven CLI Verification
Naye Command Prompt mein Maven version verify karein:
```cmd
C:\Users\numl-> mvn -version
Apache Maven 3.9.6
Maven home: C:\Tools\apache-maven
Java version: 17.0.12, vendor: Eclipse Adoptium, runtime: C:\Java\jdk-17
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 3.2: Maven Version Verification]**  
> **Command:** `mvn -version`  
> **Window:** Naya Command Prompt  
> **Kya capture karna hai:** Apache Maven version aur uske niche Java version 17 ka association.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

## Part 4: Maven Build Lifecycle (compile, test, clean package)

### 4.1 Project Object Model (`pom.xml`) Check
Project folder mein jakar `pom.xml` check karein:
```cmd
cd /d "C:\Users\numl-\Desktop\student-task-manager\student-task-manager"
dir pom.xml
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 4.1: dir pom.xml Verification]**  
> **Command:** `dir pom.xml`  
> **Window:** Command Prompt (project folder mein)  
> **Kya capture karna hai:** `pom.xml` file ka directory record aur size.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 4.2 Compilation Phase (`mvn compile`)
Source code ko compile karein:
```cmd
mvn compile
[INFO] Compiling 1 source file with javac [debug target 17] to target\classes
[INFO] BUILD SUCCESS
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 4.2: mvn compile BUILD SUCCESS]**  
> **Command:** `mvn compile`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** `Compiling 1 source file...` aur `[INFO] BUILD SUCCESS`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 4.3 Automated Testing Phase (`mvn test`)
JUnit 5 automated tests execute karein:
```cmd
mvn test
[INFO] Running com.student.TaskServiceTest
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 4.3: mvn test Results]**  
> **Command:** `mvn test`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** `Tests run: 4, Failures: 0, Errors: 0` aur `BUILD SUCCESS`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 4.4 Packaging Phase (`mvn clean package`)
Complete WAR file package banayein:
```cmd
mvn clean package
[INFO] Assembling webapp [student-task-manager] in [target\student-task-manager]
[INFO] Building war: ...\target\student-task-manager.war
[INFO] BUILD SUCCESS
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 4.4: mvn clean package WAR Building]**  
> **Command:** `mvn clean package`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** `Building war: ...\student-task-manager.war` aur `BUILD SUCCESS`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 4.5 Target WAR Verification
Target folder mein `student-task-manager.war` verify karein:
```cmd
dir target\*.war
10/12/2026  07:30 PM            24,850 student-task-manager.war
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 4.5: dir target\*.war Check]**  
> **Command:** `dir target\*.war`  
> **Window:** Command Prompt  
> **Kya capture karna hai:** `student-task-manager.war` file ka listing aur size.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

## Part 5: Apache Tomcat Setup aur Browser Verification

### 5.1 WAR Copy to Tomcat `webapps`
Generated WAR file ko `C:\Tomcat\webapps\` mein copy karein:
```cmd
copy target\student-task-manager.war C:\Tomcat\webapps\
        1 file(s) copied.
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 5.1: Copying WAR to Tomcat webapps]**  
> **Command:** `copy target\student-task-manager.war C:\Tomcat\webapps\`  
> **Window:** Command Prompt (ya Windows File Explorer mein `C:\Tomcat\webapps` folder)  
> **Kya capture karna hai:** File copy confirmation message `1 file(s) copied`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 5.2 Tomcat Server Startup (`catalina.bat run`)
Tomcat server ko console mode mein launch karein:
```cmd
set "JAVA_HOME=C:\Java\jdk-17"
set "PATH=%JAVA_HOME%\bin;%PATH%"
cd /d C:\Tomcat\bin
catalina.bat run
```

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 5.2: Tomcat catalina.bat run Console]**  
> **Command:** `catalina.bat run`  
> **Window:** Tomcat Command Prompt Window  
> **Kya capture karna hai:** Server startup logs: `Deployment of web application archive [student-task-manager.war] has finished` aur `Starting ProtocolHandler ["http-nio-8080"]`.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 5.3 Web Browser Verification
Browser mein application load karein:  
👉 **`http://localhost:8080/student-task-manager/`**  
*(Direct static check: [`index.html`](file:///c:/Users/numl-/Desktop/student-task-manager/student-task-manager/index.html))*

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 5.3: Web Application Home Screen]**  
> **URL:** `http://localhost:8080/student-task-manager/`  
> **Window:** Chrome / Edge Browser  
> **Kya capture karna hai:** Poora browser window jahan Student Task Management System ka header, form, aur 3 default tasks dikh rahi hon.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

### 5.4 Functional Testing (Task Addition)
Webpage par nayi task enter karein aur add karein:
- **Title:** `Complete DevOps Assignment Report`
- **Description:** `Deploy WAR file to Apache Tomcat 10.1`
- **Priority:** `High`
- Click: `+ Add Task`

> 📸 **[SCREENSHOT PLACEHOLDER — Figure 5.4: Dynamic Task Added & Counter Updated]**  
> **Window:** Browser Window  
> **Kya capture karna hai:** List mein nayi task show ho rahi ho aur counter badge 3 se update hokar `4` ho chuka ho.  
> **Shortcuts:** `Win + Shift + S` se snip karein -> Word mein paste karein.

---

## 🛠️ Common Problems & Solutions

| Issue / Error | Wajah (Root Cause) | Solution (Hal) |
|---|---|---|
| **Port 8080 busy / conflict** | Jenkins ya IIS port 8080 use kar raha hai. | `C:\Tomcat\conf\server.xml` kholein, `<Connector port="8080"` ko change karke `8081` karein, Tomcat restart karein aur `http://localhost:8081/student-task-manager/` kholein. |
| **`mvn` is not recognized** | `C:\Tools\apache-maven\bin` Path mein add nahi hai ya naya terminal nahi khola. | Environment Variables -> Path mein `C:\Tools\apache-maven\bin` check karein aur Command Prompt restart karein. |
| **Maven galat Java dikha raha hai** | `JAVA_HOME` purane JDK/JRE par set hai. | System Variable `JAVA_HOME` ko `C:\Java\jdk-17` karein aur `echo %JAVA_HOME%` se confirm karein. |
| **404 Not Found error** | WAR file ka naam galat hai ya context root match nahi kar raha. | WAR ka naam bilkul `student-task-manager.war` rakhein aur Tomcat ke console log mein deployment check karein. |
