package org.acme.testcoverage;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HelloResourceTest {

    @Test
    public void testHelloEndpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.hello();

        assertEquals(response, expectedList);
    }
}