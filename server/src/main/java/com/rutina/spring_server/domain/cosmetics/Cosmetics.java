package com.rutina.spring_server.domain.cosmetics;

import lombok.Getter;

import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;

@Getter
@Entity
@Table(name = "api_cosmetics")
public class Cosmetics {

    @EmbeddedId
    private CosmeticsId id;

}
