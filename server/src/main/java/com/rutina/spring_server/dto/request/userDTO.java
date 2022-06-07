package com.rutina.spring_server.dto.request;

import lombok.Getter;

import java.util.Date;


public class userDTO {
    private String id;
    private String pwd;
    private String name;
    private Date birthday;
    private int gender;
    private String nickname;
    private int question;
    private String questionAnswer;
    private int skinType;
    private String skinAgonize;

}
