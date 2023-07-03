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


}