import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';

// Define an enum for HTTP methods
enum HttpMethod {
    GET = 'get',
    POST = 'post',
    PUT = 'put',
    DELETE = 'delete',
}

async function sendRequest(
    endpoint: string,
    idToken: string,
    method: HttpMethod = HttpMethod.GET,
    data?: any
): Promise<AxiosResponse> {
    const config: AxiosRequestConfig = {
        method,
        url: `http://localhost:5000/${endpoint}`,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`,
        },
        data,
    };

    try {
        const response = await axios(config);
        return response;
    } catch (error) {
        // Handle error, e.g., log it or throw a custom error
        console.error(`Error during ${method.toUpperCase()} request to ${endpoint}:`, error);
        throw error;
    }
}

export async function login(idToken: string): Promise<AxiosResponse> {
    return sendRequest('login', idToken, HttpMethod.POST);
}
