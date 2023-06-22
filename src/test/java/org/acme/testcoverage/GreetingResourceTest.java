package org.acme.testcoverage;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

public class GreetingResourceTest {

    @Mock
    private GreetingService greetingService;

    private GreetingResource greetingResource;

    @BeforeEach
    public void setup() {
        MockitoAnnotations.openMocks(this);
        greetingResource = new GreetingResource(greetingService);
    }

    @Test
    public void testGreetingEndpoint() {
        String name = "Alice";
        String expectedResponse = "hello Alice";

        when(greetingService.greeting(name)).thenReturn(expectedResponse);

        String response = greetingResource.greeting(name);

        assertEquals(expectedResponse, response);
        verify(greetingService).greeting(name);
    }

    @Test
    public void testHelloEndpoint() {
        String expectedResponse = "hello";

        String response = greetingResource.hello();

        assertEquals(expectedResponse, response);
    }
}