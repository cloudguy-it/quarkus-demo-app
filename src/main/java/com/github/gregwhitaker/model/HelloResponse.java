package com.github.gregwhitaker.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import io.quarkus.runtime.annotations.RegisterForReflection;

// This @RegisterForReflection method is required when building native image and the annotated object
// is returned from a method, but the return type of that method is not this object. So in the case of this response object
// we are returning a javax.ws.rs.core.Response object with this as the body. If you do not annotated this method for reflection
// the response body will always return empty.
@RegisterForReflection
@JsonPropertyOrder({
        "createTime",
        "message"
})
public class HelloResponse {

    @JsonProperty("create_time") private String createTime;
    private String message;

    public String getCreateTime() {
        return createTime;
    }

    public void setCreateTime(String createTime) {
        this.createTime = createTime;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
