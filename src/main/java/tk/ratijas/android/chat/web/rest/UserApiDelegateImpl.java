package tk.ratijas.android.chat.web.rest;

import org.springframework.stereotype.Service;
import org.springframework.web.context.request.NativeWebRequest;
import tk.ratijas.android.chat.web.api.UserApiDelegate;
import tk.ratijas.android.chat.web.api.UsersApiDelegate;

import java.util.Optional;

@Service
public class UserApiDelegateImpl implements UserApiDelegate, UsersApiDelegate {
    private final NativeWebRequest request;

    public UserApiDelegateImpl(NativeWebRequest request) {
        this.request = request;
    }

    @Override
    public Optional<NativeWebRequest> getRequest() {
        return Optional.ofNullable(request);
    }
}
