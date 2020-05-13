package tk.ratijas.android.chat.service;

import tk.ratijas.android.chat.domain.SmsVerificationCode;
import tk.ratijas.android.chat.repository.SmsVerificationCodeRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

/**
 * Service Implementation for managing {@link SmsVerificationCode}.
 */
@Service
@Transactional
public class SmsVerificationCodeService {

    private final Logger log = LoggerFactory.getLogger(SmsVerificationCodeService.class);

    private final SmsVerificationCodeRepository smsVerificationCodeRepository;

    public SmsVerificationCodeService(SmsVerificationCodeRepository smsVerificationCodeRepository) {
        this.smsVerificationCodeRepository = smsVerificationCodeRepository;
    }

    /**
     * Save a smsVerificationCode.
     *
     * @param smsVerificationCode the entity to save.
     * @return the persisted entity.
     */
    public SmsVerificationCode save(SmsVerificationCode smsVerificationCode) {
        log.debug("Request to save SmsVerificationCode : {}", smsVerificationCode);
        return smsVerificationCodeRepository.save(smsVerificationCode);
    }

    /**
     * Get all the smsVerificationCodes.
     *
     * @return the list of entities.
     */
    @Transactional(readOnly = true)
    public List<SmsVerificationCode> findAll() {
        log.debug("Request to get all SmsVerificationCodes");
        return smsVerificationCodeRepository.findAll();
    }

    /**
     * Get one smsVerificationCode by id.
     *
     * @param id the id of the entity.
     * @return the entity.
     */
    @Transactional(readOnly = true)
    public Optional<SmsVerificationCode> findOne(Long id) {
        log.debug("Request to get SmsVerificationCode : {}", id);
        return smsVerificationCodeRepository.findById(id);
    }

    /**
     * Delete the smsVerificationCode by id.
     *
     * @param id the id of the entity.
     */
    public void delete(Long id) {
        log.debug("Request to delete SmsVerificationCode : {}", id);
        smsVerificationCodeRepository.deleteById(id);
    }
}
