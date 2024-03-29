package org.acme.testcoverage;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.Arrays;
import java.util.List;

@Path("/hi")
public class HelloResource {

    List<String> list = Arrays.asList("A", "B", "C");

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> hello() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> bye() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> greetings() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> morning() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> day() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> test1() {
        //return "Hello RESTEasy";
        return list;
    }

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public List<String> test2() {
        //return "Hello RESTEasy";
        return list;
    }


}