package com.rutina.spring_server.controller;

import com.rutina.spring_server.domain.users.Users;
import com.rutina.spring_server.domain.users.UsersRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Optional;

@RestController
@RequestMapping(value="/users")
public class UsersController {

    private UsersRepository usersRep;

    @Autowired
    public UsersController(UsersRepository usersRep) {
        this.usersRep = usersRep;
    }

    //테이블 리스트 가져오기
    @GetMapping
    public Iterable<Users> list() throws Exception{
        return usersRep.findAll();
    }

    //id로 테이블 값 가져오기
    @GetMapping(value = "/{id}")
    public Optional<Users> findOne(@PathVariable String id) throws Exception {
        return usersRep.findById(id);
    }


}
