
void DCT4SetPhoneMenus	   (int argc, char *argv[]);
void DCT4tests		   (int argc, char *argv[]);
void DCT4SetVibraLevel	   (int argc, char *argv[]);
void DCT4ResetSecurityCode (int argc, char *argv[]);
void DCT4GetVoiceRecord	   (int argc, char *argv[]);
void DCT4Info		   (int argc, char *argv[]);

/* ------------------- features matrix ------------------------------------- */

typedef enum {
	DCT4_ALWAYS_ONLINE = 1,
	DCT4_GPRS_PCCH,
	DCT4_GEA1,
	DCT4_EOTD,
	DCT4_WAP_PUSH,
	DCT4_USE_PREF_SIM_NET,

	DCT4_ALS,
	DCT4_A52,
	DCT4_CSP,
	DCT4_DISPLAY_PHONE_NAME,
	DCT4_DISPLAY_WAP_PROFILE,

	DCT4_GAMES_WAP_DOWNLOAD,
	DCT4_GAMES_SCORE_SEND,
	DCT4_GAMES_URL_CHECK,

	DCT4_BLUETOOTH_MENU,
	DCT4_WAP_BOOKMARKS_MENU,
	DCT4_WAP_GOTO_MENU,
	DCT4_WAP_SETTINGS_MENU,
	DCT4_SERVICES_GAMES_APP_GALLERY,
	DCT4_JAVA_GAMES_MENU,
	DCT4_SAT_CONFIRM_MENU,

	DCT4_TEST
} DCT4_Feature_Name;

typedef struct {
	DCT4_Feature_Name		Name;
	unsigned char			*Text;
	struct {
		unsigned char		Value;
		unsigned char		*Text;
	} Values[10];
} DCT4_Feature;

typedef struct {
	char				*Model;
	struct {
		DCT4_Feature_Name	Name;
		int			Number;
	} Features[25];
} DCT4_Phone_Features;

/* ------------------------------------------------------------------------- */

/* How should editor hadle tabs in this file? Add editor commands here.
 * vim: noexpandtab sw=8 ts=8 sts=8:
 */
