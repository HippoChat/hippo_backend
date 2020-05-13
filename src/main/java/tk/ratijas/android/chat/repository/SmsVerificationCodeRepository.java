package tk.ratijas.android.chat.repository;

import tk.ratijas.android.chat.domain.SmsVerificationCode;

import org.springframework.data.jpa.repository.*;
import org.springframework.stereotype.Repository;

/**
 * Spring Data  repository for the SmsVerificationCode entity.
 */
@SuppressWarnings("unused")
@Repository
public interface SmsVerificationCodeRepository extends JpaRepository<SmsVerificationCode, Long> {
}
