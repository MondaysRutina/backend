package com.rutina.spring_server.dto.request;

import lombok.Getter;

@Getter // 안돌아가면 빼기
public class cosmeticsDTO {
    private String apiCosmeticType;
    private String apiCosmeticName;
    private String apiCosmeticPh;
}
