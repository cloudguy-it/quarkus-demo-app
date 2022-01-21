package com.github.gregwhitaker;

import com.github.gregwhitaker.model.HelloResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.DefaultValue;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Simple Hello World Resource
 */
@Path("/hello")
public class HelloResource {
    private static final Logger LOG = LoggerFactory.getLogger(HelloResource.class);

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response hello(@DefaultValue("You") @QueryParam("name") String name) {
        LOG.info("Received hello request for: {}", name);

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");

        HelloResponse body = new HelloResponse();
        body.setCreateTime(sdf.format(new Date()));
        body.setMessage(String.format("Hello, %s!", name));

        return Response.ok(body)
                .encoding(MediaType.APPLICATION_JSON)
                .build();
    }
}