# gemini_integration.jac

import:py gemini_helper;

with entry {
    joke = gemini_helper.get_joke();
    print(joke);
}
