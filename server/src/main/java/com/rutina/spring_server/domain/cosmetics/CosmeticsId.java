package com.rutina.spring_server.domain.cosmetics;

import lombok.*;

import javax.persistence.Column;
import javax.persistence.Embeddable;
import java.io.Serializable;

@Embeddable
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@EqualsAndHashCode
public class CosmeticsId implements Serializable {

    @Column(name = "api_cosmetic_type")
    private String apiCosmeticType;

    @Column(name = "api_cosmetic_name")
    private String apiCosmeticName;

    @Column(name = "api_cosmetic_ph")
    private String apiCosmeticPh;

    /*public Cosmetics(){}

    public Cosmetics(String apiCosmeticType,String apiCosmeticName, String apiCosmeticPh){
        this.apiCosmeticType = apiCosmeticType;
        this.apiCosmeticName = apiCosmeticName;
        this.apiCosmeticPh = apiCosmeticPh;
    }*/
}
