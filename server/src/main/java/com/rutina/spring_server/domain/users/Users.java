package com.rutina.spring_server.domain.users;

import lombok.Getter;

import javax.persistence.*;

@Getter
@Entity
@Table(name = "user")
public class Users {
    @Id @GeneratedValue
    private String id;
    private String name;

    public Users(){}

    public Users(String id, String name){
        this.id = id;
        this.name = name;
    }

}


