package tk.ratijas.android.chat.domain;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;
import tk.ratijas.android.chat.web.rest.TestUtil;

public class SmsVerificationCodeTest {

    @Test
    public void equalsVerifier() throws Exception {
        TestUtil.equalsVerifier(SmsVerificationCode.class);
        SmsVerificationCode smsVerificationCode1 = new SmsVerificationCode();
        smsVerificationCode1.setId(1L);
        SmsVerificationCode smsVerificationCode2 = new SmsVerificationCode();
        smsVerificationCode2.setId(smsVerificationCode1.getId());
        assertThat(smsVerificationCode1).isEqualTo(smsVerificationCode2);
        smsVerificationCode2.setId(2L);
        assertThat(smsVerificationCode1).isNotEqualTo(smsVerificationCode2);
        smsVerificationCode1.setId(null);
        assertThat(smsVerificationCode1).isNotEqualTo(smsVerificationCode2);
    }
}
