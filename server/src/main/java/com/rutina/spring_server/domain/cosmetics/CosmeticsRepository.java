package com.rutina.spring_server.domain.cosmetics;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CosmeticsRepository extends CrudRepository<Cosmetics, CosmeticsId> {
}
