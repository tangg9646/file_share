package com.itranswarp.learnjava;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Node;


public class Main {

	public static void main(String[] args) throws Exception {


		//这部分时读取xml文件内容的代码，可跳过不看
		// 路径以 / 开头，表示获取ClassPath路径下的文件
		System.out.println("当前类的ClassPath路径" + Main.class.getResource("/"));
		InputStream input = Main.class.getResourceAsStream("/book.xml");

		// 解析并获取Document对象:
		DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
		DocumentBuilder db = dbf.newDocumentBuilder();
		Document doc = db.parse(input);
		printNode(doc, 0);



		//查看jvm正在运行的当前路径，后续的File类的相对路径都是以这个路径为基础
		System.out.println("当前jvm运行的路径：");
		System.out.println(System.getProperty("user.dir"));

		//在当前目录创建
		File file1 = new File(".\\当前目录创建1.properties");
		file1.createNewFile();
		File file11 = new File("当前目录创建2.properties");
		file11.createNewFile();

		//在指定目录创建文件
		File file2 = new File(".\\target\\generated-sources\\在指定目录创建文件1.properties");
		file2.createNewFile();
		File file22 = new File("target\\generated-sources\\在指定目录创建文件2.properties");
		file22.createNewFile();

		try {
			System.out.println(file1.exists()+":"+file1.getCanonicalPath());
			System.out.println(file11.exists()+":"+file11.getCanonicalPath());
			System.out.println(file2.exists()+":"+file2.getCanonicalPath());
			System.out.println(file22.exists()+":"+file22.getCanonicalPath());
		} catch (IOException e) {
			e.printStackTrace();
		}


		//通过类的名称获取路径，并观察加不加 / 的不同
		System.out.println("当前类所在的包的路径：");
		System.out.println(Main.class.getResource(""));
		System.out.println("当前类的ClassPath路径（不懂得IDE可能目录结构不同）");
		System.out.println(Main.class.getResource("/"));



		//通过类的实例获取路径
		Main t= new Main();
		System.out.println("t.getClass()");
		System.out.println(t.getClass());
		System.out.println("t.getClass().getClassLoader()");
		System.out.println(t.getClass().getClassLoader());
		System.out.println("t.getClass().getClassLoader().getResource(\"\")");
		System.out.println(t.getClass().getClassLoader().getResource(""));
		System.out.println("t.getClass().getClassLoader().getResource(\"/\")");
		System.out.println(t.getClass().getClassLoader().getResource("/"));//null

	}

	static void printNode(Node n, int indent) {
		for (int i = 0; i < indent; i++) {
			System.out.print(' ');
		}
		switch (n.getNodeType()) {
			case Node.DOCUMENT_NODE:
				System.out.println("Document: " + n.getNodeName());
				break;
			case Node.ELEMENT_NODE:
				System.out.println("Element: " + n.getNodeName());
				break;
			case Node.TEXT_NODE:
				System.out.println("Text: " + n.getNodeName() + " = " + n.getNodeValue());
				break;
			case Node.ATTRIBUTE_NODE:
				System.out.println("Attr: " + n.getNodeName() + " = " + n.getNodeValue());
				break;
			case Node.CDATA_SECTION_NODE:
				System.out.println("CDATA: " + n.getNodeName() + " = " + n.getNodeValue());
				break;
			case Node.COMMENT_NODE:
				System.out.println("Comment: " + n.getNodeName() + " = " + n.getNodeValue());
				break;
			default:
				System.out.println("NodeType: " + n.getNodeType() + ", NodeName: " + n.getNodeName());
		}
		for (Node child = n.getFirstChild(); child != null; child = child.getNextSibling()) {
			printNode(child, indent + 1);
		}
	}
}
