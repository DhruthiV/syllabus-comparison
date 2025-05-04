from syllabus_comparison import compare_syllabi
old = {
  "year": "2022",
  "program": "MCA",
  "course_code": "UQ22CA751A",
  "course_content": {
    "unit1": {
      "title": "Java Fundamentals",
      "topics": [
        "Object-Oriented Programming",
        "JDK",
        "Data types",
        "Operators",
        "Program control statements - if",
        "Program control statements - switch",
        "Program control statements - for",
        "Program control statements - while",
        "Classes",
        "Objects and Methods",
        "Myths and Facts about Java classes and objects",
        "Constructors",
        "Static and Heap memory",
        "new keyword",
        "Garbage Collection and finalizers",
        "this keyword",
        "Arrays and jagged arrays",
        "Array References",
        "length Member",
        "for loops",
        "for-each",
        "Strings",
        "Command-Line Arguments",
        "Method Overloading",
        "Overloading Constructors",
        "Nested Classes."
      ],
      "experiential_learning": [
        "Problem solving with data types",
        "Loops",
        "Arrays",
        "Garbage Collection",
        "Polymorphism."
      ]
    },
    "unit2": {
      "title": "Inheritance and Multithreading",
      "topics": [
        "Inheritance",
        "Member Access",
        "Constructors",
        "Method Overriding",
        "Abstract Classes",
        "Exception Handling",
        "Interfaces and Packages",
        "Multithreaded Programming",
        "Thread Communication Using notify()",
        "wait() and notifyAll()",
        "String Handling",
        "Enumeration and Annotations",
        "Wrappers Class."
      ],
      "experiential_learning": [
        "Problem solving with Inheritance",
        "Exception handling",
        "Multi-threading",
        "Annotations."
      ]
    },
    "unit3": {
      "title": "JDBC and Servlets",
      "topics": [
        "JDBC classes and interfaces",
        "Talking to Database",
        "Immediate Solution",
        "Essential JDBC program",
        "Using Prepared Statement Object",
        "Interactive SQL Tool",
        "types of JDBC",
        "JDBC in Action - Result Sets",
        "JDBC in Action - Batch updates",
        "JDBC in Action - Mapping",
        "JDBC in Action - Basic JDBC data types",
        "JDBC in Action - Advanced JDBC datatypes",
        "JDBC in Action - Immediate Solutions",
        "Web Application Server",
        "Server Architecture",
        "Servlet Structure",
        "Servlet Creation",
        "Servlet's Lifecycle",
        "Single Thread model interface",
        "Handling Client Request: Form Data",
        "Handling Client Request: HTTP Request Headers",
        "Generating Server Response: HTTP Response Headers",
        "Inter-Servlet communication",
        "Handling Cookies",
        "Session Tracking."
      ],
      "experiential_learning": [
        "Problem solving JDBC",
        "Problem solving using Servlets",
        "Cookies and Sessions."
      ]
    },
    "unit4": {
      "title": "JSP, Annotations, Frameworks",
      "topics": [
        "Overview of JSP Technology",
        "Need of JSP",
        "Benefits of JSP",
        "Advantages of JSP",
        "Basic Syntax",
        "Invoking Java Code with JSP Scripting Elements",
        "Using JSP expressions",
        "Using Scriplets",
        "Declarations",
        "Creating Packages",
        "JAR files",
        "Annotations",
        "Annotation types",
        "working with Java Bean",
        "Frameworks - Hibernate",
        "Frameworks - Struts",
        "Frameworks - Spring"
      ],
      "experiential_learning": [
        "Working with JSP scripting elements",
        "annotations and creating JAR files."
      ]
    }
  }
}
news = {
  "year": "2023",
  "program": "MCA",
  "course_code": "UQ23CA751A",
  "course_content": {
    "unit1": {
      "title": "Java Fundamentals and OOP",
      "topics": [
        "Overview of Java",
        "Basic Java Concepts",
        "JDK",
        "JVM",
        "JRE",
        "Building Blocks of Java - Keywords",
        "Building Blocks of Java - Methods",
        "Building Blocks of Java - Control Flow",
        "Building Blocks of Java - Loops",
        "Building Blocks of Java - Operators",
        "Arrays",
        "Strings",
        "Introduction to OOP",
        "Classes and Objects",
        "Constructor",
        "Interfaces and Abstract Classes",
        "Inheritance in Java",
        "Polymorphism - Method Overloading",
        "Polymorphism - Method Overriding",
        "Polymorphism - Dynamic Method Dispatch",
        "Wrapper Classes and Autoboxing"
      ],
      "experiential_learning": [
        "Programs on decision making and loops",
        "Programs on Inheritance",
        "Polymorphism",
        "Programs implementing autoboxing",
        "Array and String Handling"
      ]
    },
    "unit2": {
      "title": "Advanced Java Concepts",
      "topics": [
        "Encapsulation and Access Specifiers",
        "Exception Handling",
        "Threads - Multithreading",
        "Threads - Thread Communication",
        "Collections Framework in Java - Introduction to Collections",
        "Collections Framework in Java - Map",
        "Collections Framework in Java - Set",
        "Collections Framework in Java - List",
        "Collections Framework in Java - LinkedList",
        "Collections Framework in Java - Queue",
        "Collections Framework in Java - ArrayList",
        "Uses and Applications of Collections",
        "Data Structures in Java JShell",
        "Garbage Collection"
      ],
      "experiential_learning": [
        "Programs on Access Specifiers",
        "Exception Handling",
        "JShell Scripting",
        "Multithreading",
        "Java Collections Framework",
        "Implementing Data Structures in Java"
      ]
    },
    "unit3": {
      "title": "Web Application Development with Java",
      "topics": [
        "Introduction to JSP",
        "Scriptlets",
        "Expressions",
        "Declarations",
        "Database Management - SQL and NoSQL Databases",
        "Database Management - Database Connectivity in Java with SQLite",
        "Understanding JDBC",
        "JDBC Classes and Interfaces - Connection",
        "JDBC Classes and Interfaces - DriverManager",
        "JDBC Classes and Interfaces - Statement",
        "JDBC Classes and Interfaces - PreparedStatement",
        "JDBC Classes and Interfaces - CallableStatement",
        "JDBC Classes and Interfaces - ResultSet",
        "MongoDB Operations in Java"
      ],
      "experiential_learning": [
        "Developing Database Web Application using JSP and SQLite",
        "Developing Database Web Application using JSP and MongoDB"
      ]
    },
    "unit4": {
      "title": "Java Bean and Hibernate",
      "topics": [
        "Java Bean - Introduction",
        "Java Bean - Bean Development",
        "Java Bean - Introspection",
        "Java Bean - Design Patterns of Java Beans",
        "Java Bean - Simple Properties",
        "Java Bean - Indexed Properties",
        "Java Bean - BeanInfo",
        "Java Bean - Persistence",
        "Java Bean - JavaBeans API",
        "Hibernate - Introduction",
        "Hibernate - Architecture",
        "Hibernate - Java Objects in Hibernate",
        "Hibernate - Inheritance Mapping",
        "Hibernate - Hibernate Query Language (HQL)",
        "Hibernate - Hibernate Named Query",
        "Hibernate - Associations and Relationships in ORM"
      ],
      "experiential_learning": [
        "Java Bean Development",
        "Application Development using Hibernate Framework"
      ]
    }
  }
}

result = compare_syllabi(old, news, similarity_threshold=0.6)

import json
print(json.dumps(result, indent=2))