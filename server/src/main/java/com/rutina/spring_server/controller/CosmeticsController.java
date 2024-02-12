package com.rutina.spring_server.controller;

import com.rutina.spring_server.domain.cosmetics.Cosmetics;
import com.rutina.spring_server.domain.cosmetics.CosmeticsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value="/cosmetics")
public class CosmeticsController {

    private CosmeticsRepository cosmeticsRep;

    @Autowired
    public CosmeticsController(CosmeticsRepository cosmeticsRep) {
        this.cosmeticsRep = cosmeticsRep;
    }

    // 전체 화장품 데이터 불러오기기
   @GetMapping
    public Iterable<Cosmetics> cosmeticsList() throws Exception{
        return cosmeticsRep.findAll();
    }

}
