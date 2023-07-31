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
    @Test
    public void testByeEndpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.bye();

        assertEquals(response, expectedList);
    }

    @Test
    public void testGreetingsEndpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.greetings();

        assertEquals(response, expectedList);
    }

    @Test
    public void testMorningsEndpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.morning();

        assertEquals(response, expectedList);
    }

    @Test
    public void testDayEndpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.day();

        assertEquals(response, expectedList);
    }

    @Test
    public void testTest1Endpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.test1();

        assertEquals(response, expectedList);
    }


    @Test
    public void testTest2Endpoint() {
        HelloResource helloResource = new HelloResource();
        List<String> expectedList = Arrays.asList("A", "B", "C");

        List<String> response = helloResource.test2();

        assertEquals(response, expectedList);
    }



}