import os
import sys
from datetime import datetime
import requests as req

print("[+] All imports completed successfully")

try:
    USERNAME = f'{list(os.listdir("/home/"))[0]}'
except IndexError:
    sys.exit("[-] No user folder found in /home/")


def clear():
    os.system("clear")


def better_discord_plugins(logfile):

    global USERNAME

    all_stuff = (
                ("message logger",
                 "MessageLoggerV2.plugin.js",
                 "https://cdn.discordapp.com/attachments/853817893744803840/917758026667130900/MessageLoggerV2.plugin.js",
                 "plugin"),

                ("show hidden channels",
                 "ShowHiddenChannels.plugin.js",
                 "https://betterdiscord.app/Download?id=103",
                 "plugin"),

                ("call time counter",
                 "CallTimeCounter.plugin.js",
                 "https://betterdiscord.app/Download?id=228",
                 "plugin"),

                ("discord free emojis",
                 "DiscordFreeEmojis64px.plugin.js",
                 "https://betterdiscord.app/Download?id=245",
                 "plugin"),

                ("spotify controls",
                 "SpotifyControls.plugin.js",
                 "https://betterdiscord.app/Download?id=105",
                 "plugin"),

                ("GameActivityToggle",
                 "GameActivityToggle.plugin.js",
                 "https://betterdiscord.app/Download?id=120",
                 "plugin"),

                ("Translator",
                 "Translator.plugin.js",
                 "https://betterdiscord.app/Download?id=81",
                 "plugin"),

                ("CreationDate",
                 "CreationDate.plugin.js",
                 "https://betterdiscord.app/Download?id=69",
                 "plugin"),

                ("ReadAllNotificationsButton",
                 "ReadAllNotificationsButton.plugin.js",
                 "https://betterdiscord.app/Download?id=94",
                 "plugin"),

                ("BetterVolume",
                 "BetterVolume.plugin.js",
                 "https://betterdiscord.app/Download?id=184",
                 "plugin"),

                ("BetterRoleColors",
                 "BetterRoleColors.plugin.js",
                 "https://betterdiscord.app/Download?id=2",
                 "plugin"),

                ("PluginRepo",
                 "PluginRepo.plugin.js",
                 "https://betterdiscord.app/Download?id=200",
                 "plugin"),

                ("InvisibleTyping",
                 "InvisibleTyping.plugin.js",
                 "https://betterdiscord.app/Download?id=295",
                 "plugin"),

                ("SplitLargeMessages",
                 "SplitLargeMessages.plugin.js",
                 "https://betterdiscord.app/Download?id=98",
                 "plugin"),

                ("UserVolumeBooster",
                 "UserVolumeBooster.plugin.js",
                 "https://betterdiscord.app/Download?id=272",
                 "plugin"),

                ("ImageUtilities",
                 "ImageUtilities.plugin.js",
                 "https://betterdiscord.app/Download?id=83",
                 "plugin"),

                ("HideDisabledEmojis",
                 "HideDisabledEmojis.plugin.js",
                 "https://betterdiscord.app/Download?id=188",
                 "plugin"),

                ("ShowBadgesInChat",
                 "ShowBadgesInChat.plugin.js",
                 "https://betterdiscord.app/Download?id=60",
                 "plugin"),

                ("TypingUsersAvatars",
                 "TypingUsersAvatars.plugin.js",
                 "https://betterdiscord.app/Download?id=253",
                 "plugin"),

                ("PermissionsViewer",
                 "PermissionsViewer.plugin.js",
                 "https://betterdiscord.app/Download?id=29",
                 "plugin"),

        ("AppNotifications",
                    "AppNotifications.plugin.js",
                    "https://betterdiscord.app/Download?id=173",
                    "plugin"),

        ("ServerDetails",
                    "ServerDetails.plugin.js",
                    "https://betterdiscord.app/Download?id=100",
                    "plugin"),

        ("TypingIndicator",
                    "TypingIndicator.plugin.js",
                    "https://betterdiscord.app/Download?id=196",
                    "plugin"),

        ("ThemeRepo",
                    "ThemeRepo.plugin.js",
                    "https://betterdiscord.app/Download?id=201",
                    "plugin"),

        ("FriendNotifications",
                    "FriendNotifications.plugin.js",
                    "https://betterdiscord.app/Download?id=86",
                    "plugin"),

        ("ZeresPluginLibrary",
                    "ZeresPluginLibrary.plugin.js",
                    "https://betterdiscord.app/Download?id=9",
                    "plugin"),

        ("AutoStartRichPresence",
                    "AutoStartRichPresence.plugin.js",
                    "https://betterdiscord.app/Download?id=238",
                    "plugin"),

        ("NotificationSounds",
                    "NotificationSounds.plugin.js",
                    "https://betterdiscord.app/Download?id=88",
                    "plugin"),

        ("DoubleClickToEdit",
                    "DoubleClickToEdit.plugin.js",
                    "https://betterdiscord.app/Download?id=354",
                    "plugin"),

        ("WhoReacted",
                    "WhoReacted.plugin.js",
                    "https://betterdiscord.app/Download?id=138",
                    "plugin"),

        ("QuickMention",
                    "QuickMention.plugin.js",
                    "https://betterdiscord.app/Download?id=93",
                    "plugin"),

        ("BetterFriendList",
                    "BetterFriendList.plugin.js",
                    "https://betterdiscord.app/Download?id=61",
                    "plugin"),

        ("AssignBadges",
                    "AssignBadges.plugin.js",
                    "https://betterdiscord.app/Download?id=336",
                    "plugin"),

        ("StaffTag",
                    "StaffTag.plugin.js",
                    "https://betterdiscord.app/Download?id=162",
                    "plugin"),

        ("ShowConnections",
                    "ShowConnections.plugin.js",
                    "https://betterdiscord.app/Download?id=291",
                    "plugin"),

        ("JoinedAtDate",
                    "JoinedAtDate.plugin.js",
                    "https://betterdiscord.app/Download?id=84",
                    "plugin"),

        ("BetterFormattingRedux",
                    "BetterFormattingRedux.plugin.js",
                    "https://betterdiscord.app/Download?id=193",
                    "plugin"),

        ("LinkBanner",
                    "LinkBanner.plugin.js",
                    "https://betterdiscord.app/Download?id=340",
                    "plugin"),

        ("OnlineFriendCount",
                    "OnlineFriendCount.plugin.js",
                    "https://betterdiscord.app/Download?id=183",
                    "plugin"),

        ("BDFDB",
                    "BDFDB.plugin.js",
                    "https://betterdiscord.app/Download?id=59",
                    "plugin"),

        ("EditUsers",
                    "EditUsers.plugin.js",
                    "https://betterdiscord.app/Download?id=76",
                    "plugin"),

        ("BiggerStreamPreview",
                    "BiggerStreamPreview.plugin.js",
                    "https://betterdiscord.app/Download?id=137",
                    "plugin"),

        ("BetterNsfwTag",
                    "BetterNsfwTag.plugin.js",
                    "https://betterdiscord.app/Download?id=62",
                    "plugin"),

        ("SecretRingTone",
                    "SecretRingTone.plugin.js",
                    "https://betterdiscord.app/Download?id=139",
                    "plugin"),

        ("GuildProfile",
                    "GuildProfile.plugin.js",
                    "https://betterdiscord.app/Download?id=220",
                    "plugin"),

        ("CharCounter",
                    "CharCounter.plugin.js",
                    "https://betterdiscord.app/Download?id=64",
                    "plugin"),

        ("ThemeSettings",
                    "ThemeSettings.plugin.js",
                    "https://betterdiscord.app/Download?id=107",
                    "plugin"),

        ("ServerCounter",
                    "ServerCounter.plugin.js",
                    "https://betterdiscord.app/Download?id=99",
                    "plugin"),

        ("SpellCheck",
                    "SpellCheck.plugin.js",
                    "https://betterdiscord.app/Download?id=104",
                    "plugin"),

        ("MemberCount",
                    "MemberCount.plugin.js",
                    "https://betterdiscord.app/Download?id=11",
                    "plugin"),

        ("UserDetails",
                    "UserDetails.plugin.js",
                    "https://betterdiscord.app/Download?id=293",
                    "plugin"),

        ("CustomStatusPresets",
                    "CustomStatusPresets.plugin.js",
                    "https://betterdiscord.app/Download?id=71",
                    "plugin"),

        ("PlatformIndicators",
                    "PlatformIndicators.plugin.js",
                    "https://betterdiscord.app/Download?id=158",
                    "plugin"),

        ("NoSpotifyPause",
                    "NoSpotifyPause.plugin.js",
                    "https://betterdiscord.app/Download?id=131",
                    "plugin"),

        ("SpotifyListenAlong",
                    "SpotifyListenAlong.plugin.js",
                    "https://betterdiscord.app/Download?id=350",
                    "plugin"),

        ("LastMessageDate",
                    "LastMessageDate.plugin.js",
                    "https://betterdiscord.app/Download?id=85",
                    "plugin"),

        ("BetterFolders",
                    "BetterFolders.plugin.js",
                    "https://betterdiscord.app/Download?id=181",
                    "plugin"),

        ("WriteUppercase",
                    "WriteUppercase.plugin.js",
                    "https://betterdiscord.app/Download?id=111",
                    "plugin"),

        ("GrammarCorrect",
                    "GrammarCorrect.plugin.js",
                    "https://betterdiscord.app/Download?id=284",
                    "plugin"),

        ("DoNotTrack",
                    "DoNotTrack.plugin.js",
                    "https://betterdiscord.app/Download?id=186",
                    "plugin"),

        ("EmojiUtilities",
                    "EmojiUtilities.plugin.js",
                    "https://betterdiscord.app/Download?id=187",
                    "plugin"),

        ("BlurNSFW",
                    "BlurNSFW.plugin.js",
                    "https://betterdiscord.app/Download?id=28",
                    "plugin"),

        ("StatusEverywhere",
                    "StatusEverywhere.plugin.js",
                    "https://betterdiscord.app/Download?id=7",
                    "plugin"),

        ("ShowAllMessageButtons",
                    "ShowAllMessageButtons.plugin.js",
                    "https://betterdiscord.app/Download?id=146",
                    "plugin"),

        ("Freemoji",
                    "Freemoji.plugin.js",
                    "https://betterdiscord.app/Download?id=361",
                    "plugin"),

        ("RemoveBlockedUsers",
                    "RemoveBlockedUsers.plugin.js",
                    "https://betterdiscord.app/Download?id=95",
                    "plugin"),

        ("PinDMs",
                    "PinDMs.plugin.js",
                    "https://betterdiscord.app/Download?id=92",
                    "plugin"),

        ("Link-Profile-Picture",
                    "Link-Profile-Picture.plugin.js",
                    "https://betterdiscord.app/Download?id=287",
                    "plugin"),

        ("BetterSearchPage",
                    "BetterSearchPage.plugin.js",
                    "https://betterdiscord.app/Download?id=63",
                    "plugin"),

        ("ShowAllActivities",
                    "ShowAllActivities.plugin.js",
                    "https://betterdiscord.app/Download?id=159",
                    "plugin"),

        ("RoleMembers",
                    "RoleMembers.plugin.js",
                    "https://betterdiscord.app/Download?id=190",
                    "plugin"),

        ("AccountDetailsPlus",
                    "AccountDetailsPlus.plugin.js",
                    "https://betterdiscord.app/Download?id=31",
                    "plugin"),

        ("HideChannels",
                    "HideChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=353",
                    "plugin"),

        ("CopyRoleColors",
                    "CopyRoleColors.plugin.js",
                    "https://betterdiscord.app/Download?id=133",
                    "plugin"),

        ("CompleteTimestamps",
                    "CompleteTimestamps.plugin.js",
                    "https://betterdiscord.app/Download?id=67",
                    "plugin"),

        ("DiscordActivities",
                    "DiscordActivities.plugin.js",
                    "https://betterdiscord.app/Download?id=407",
                    "plugin"),

        ("Copier",
                    "Copier.plugin.js",
                    "https://betterdiscord.app/Download?id=176",
                    "plugin"),

        ("ChannelTabs",
                    "ChannelTabs.plugin.js",
                    "https://betterdiscord.app/Download?id=195",
                    "plugin"),

        ("ServerFolders",
                    "ServerFolders.plugin.js",
                    "https://betterdiscord.app/Download?id=101",
                    "plugin"),

        ("ChannelPermissions",
                    "ChannelPermissions.plugin.js",
                    "https://betterdiscord.app/Download?id=262",
                    "plugin"),

        ("ChatFilter",
                    "ChatFilter.plugin.js",
                    "https://betterdiscord.app/Download?id=66",
                    "plugin"),

        ("EditRoles",
                    "EditRoles.plugin.js",
                    "https://betterdiscord.app/Download?id=127",
                    "plugin"),

        ("TopRoleEverywhere",
                    "TopRoleEverywhere.plugin.js",
                    "https://betterdiscord.app/Download?id=109",
                    "plugin"),

        ("MessageUtilities",
                    "MessageUtilities.plugin.js",
                    "https://betterdiscord.app/Download?id=87",
                    "plugin"),

        ("DateViewer",
                    "DateViewer.plugin.js",
                    "https://betterdiscord.app/Download?id=236",
                    "plugin"),

        ("ServerSearch",
                    "ServerSearch.plugin.js",
                    "https://betterdiscord.app/Download?id=192",
                    "plugin"),

        ("OpenInYouTube",
                    "OpenInYouTube.plugin.js",
                    "https://betterdiscord.app/Download?id=370",
                    "plugin"),

        ("EditServers",
                    "EditServers.plugin.js",
                    "https://betterdiscord.app/Download?id=75",
                    "plugin"),

        ("DiscordExperiments",
                    "DiscordExperiments.plugin.js",
                    "https://betterdiscord.app/Download?id=206",
                    "plugin"),

        ("VoiceUsersCounter",
                    "VoiceUsersCounter.plugin.js",
                    "https://betterdiscord.app/Download?id=160",
                    "plugin"),

        ("SilentTyping(Legacy)",
                    "SilentTyping(Legacy).plugin.js",
                    "https://betterdiscord.app/Download?id=237",
                    "plugin"),

        ("PersonalPins",
                    "PersonalPins.plugin.js",
                    "https://betterdiscord.app/Download?id=91",
                    "plugin"),

        ("FavoriteMedia",
                    "FavoriteMedia.plugin.js",
                    "https://betterdiscord.app/Download?id=331",
                    "plugin"),

        ("CopyRawMessage",
                    "CopyRawMessage.plugin.js",
                    "https://betterdiscord.app/Download?id=68",
                    "plugin"),

        ("ServerHider",
                    "ServerHider.plugin.js",
                    "https://betterdiscord.app/Download?id=102",
                    "plugin"),

        ("HideStreamPreview",
                    "HideStreamPreview.plugin.js",
                    "https://betterdiscord.app/Download?id=442",
                    "plugin"),

        ("EmoteReplacer",
                    "EmoteReplacer.plugin.js",
                    "https://betterdiscord.app/Download?id=132",
                    "plugin"),

        ("GuildAndFriendRemovalAlerts",
                    "GuildAndFriendRemovalAlerts.plugin.js",
                    "https://betterdiscord.app/Download?id=317",
                    "plugin"),

        ("OpenSteamLinksInApp",
                    "OpenSteamLinksInApp.plugin.js",
                    "https://betterdiscord.app/Download?id=106",
                    "plugin"),

        ("AvatarHover",
                    "AvatarHover.plugin.js",
                    "https://betterdiscord.app/Download?id=134",
                    "plugin"),

        ("EditChannels",
                    "EditChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=74",
                    "plugin"),

        ("OldTitlebar",
                    "OldTitlebar.plugin.js",
                    "https://betterdiscord.app/Download?id=89",
                    "plugin"),

        ("AutoPlayGifs",
                    "AutoPlayGifs.plugin.js",
                    "https://betterdiscord.app/Download?id=441",
                    "plugin"),

        ("BetterMediaPlayer",
                    "BetterMediaPlayer.plugin.js",
                    "https://betterdiscord.app/Download?id=377",
                    "plugin"),

        ("RevealAllSpoilers",
                    "RevealAllSpoilers.plugin.js",
                    "https://betterdiscord.app/Download?id=97",
                    "plugin"),

        ("Zalgo",
                    "Zalgo.plugin.js",
                    "https://betterdiscord.app/Download?id=240",
                    "plugin"),

        ("DisplayServersAsChannels",
                    "DisplayServersAsChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=73",
                    "plugin"),

        ("HideChatIcons",
                    "HideChatIcons.plugin.js",
                    "https://betterdiscord.app/Download?id=356",
                    "plugin"),

        ("BetterBannedUsers",
                    "BetterBannedUsers.plugin.js",
                    "https://betterdiscord.app/Download?id=314",
                    "plugin"),

        ("GoogleSearchReplace",
                    "GoogleSearchReplace.plugin.js",
                    "https://betterdiscord.app/Download?id=80",
                    "plugin"),

        ("QuickLastMessage",
                    "QuickLastMessage.plugin.js",
                    "https://betterdiscord.app/Download?id=197",
                    "plugin"),

        ("SendButton",
                    "SendButton.plugin.js",
                    "https://betterdiscord.app/Download?id=191",
                    "plugin"),

        ("DndWhilePlaying",
                    "DndWhilePlaying.plugin.js",
                    "https://betterdiscord.app/Download?id=122",
                    "plugin"),

        ("GoogleFonts",
                    "GoogleFonts.plugin.js",
                    "https://betterdiscord.app/Download?id=457",
                    "plugin"),

        ("ColorTooltips",
                    "ColorTooltips.plugin.js",
                    "https://betterdiscord.app/Download?id=471",
                    "plugin"),

        ("ClickToCopyUsername",
                    "ClickToCopyUsername.plugin.js",
                    "https://betterdiscord.app/Download?id=164",
                    "plugin"),

        ("PlatformEmulator",
                    "PlatformEmulator.plugin.js",
                    "https://betterdiscord.app/Download?id=438",
                    "plugin"),

        ("BDContextMenu",
                    "BDContextMenu.plugin.js",
                    "https://betterdiscord.app/Download?id=185",
                    "plugin"),

        ("RemoveNicknames",
                    "RemoveNicknames.plugin.js",
                    "https://betterdiscord.app/Download?id=96",
                    "plugin"),

        ("RightClicktoJoin",
                    "RightClicktoJoin.plugin.js",
                    "https://betterdiscord.app/Download?id=312",
                    "plugin"),

        ("PronounDB",
                    "PronounDB.plugin.js",
                    "https://betterdiscord.app/Download?id=274",
                    "plugin"),

        ("SuppressReplyMentions",
                    "SuppressReplyMentions.plugin.js",
                    "https://betterdiscord.app/Download?id=8",
                    "plugin"),

        ("FileViewer",
                    "FileViewer.plugin.js",
                    "https://betterdiscord.app/Download?id=479",
                    "plugin"),

        ("ColorSighted",
                    "ColorSighted.plugin.js",
                    "https://betterdiscord.app/Download?id=323",
                    "plugin"),

        ("EmojiStatistics",
                    "EmojiStatistics.plugin.js",
                    "https://betterdiscord.app/Download?id=77",
                    "plugin"),

        ("ShowSessions",
                    "ShowSessions.plugin.js",
                    "https://betterdiscord.app/Download?id=390",
                    "plugin"),

        ("VoiceChatNotifications",
                    "VoiceChatNotifications.plugin.js",
                    "https://betterdiscord.app/Download?id=292",
                    "plugin"),

        ("QuickMessages",
                    "QuickMessages.plugin.js",
                    "https://betterdiscord.app/Download?id=116",
                    "plugin"),

        ("Apate",
                    "Apate.plugin.js",
                    "https://betterdiscord.app/Download?id=446",
                    "plugin"),

        ("NoReplyMention",
                    "NoReplyMention.plugin.js",
                    "https://betterdiscord.app/Download?id=247",
                    "plugin"),

        ("ForceImagePreviews",
                    "ForceImagePreviews.plugin.js",
                    "https://betterdiscord.app/Download?id=78",
                    "plugin"),

        ("ShutUpClyde",
                    "ShutUpClyde.plugin.js",
                    "https://betterdiscord.app/Download?id=306",
                    "plugin"),

        ("GlobalReplies",
                    "GlobalReplies.plugin.js",
                    "https://betterdiscord.app/Download?id=301",
                    "plugin"),

        ("RemoveChatButtons",
                    "RemoveChatButtons.plugin.js",
                    "https://betterdiscord.app/Download?id=383",
                    "plugin"),

        ("UserVoiceShow",
                    "UserVoiceShow.plugin.js",
                    "https://betterdiscord.app/Download?id=381",
                    "plugin"),

        ("CollapsibleUI",
                    "CollapsibleUI.plugin.js",
                    "https://betterdiscord.app/Download?id=366",
                    "plugin"),

        ("SendTimestamps",
                    "SendTimestamps.plugin.js",
                    "https://betterdiscord.app/Download?id=404",
                    "plugin"),

        ("KeywordTracker",
                    "KeywordTracker.plugin.js",
                    "https://betterdiscord.app/Download?id=318",
                    "plugin"),

        ("DashToSpaceInChannelName",
                    "DashToSpaceInChannelName.plugin.js",
                    "https://betterdiscord.app/Download?id=278",
                    "plugin"),

        ("OldUpload",
                    "OldUpload.plugin.js",
                    "https://betterdiscord.app/Download?id=349",
                    "plugin"),

        ("HideServersChannelsRedux",
                    "HideServersChannelsRedux.plugin.js",
                    "https://betterdiscord.app/Download?id=15",
                    "plugin"),

        ("KeyboardClick",
                    "KeyboardClick.plugin.js",
                    "https://betterdiscord.app/Download?id=401",
                    "plugin"),

        ("BetterCodeblocks",
                    "BetterCodeblocks.plugin.js",
                    "https://betterdiscord.app/Download?id=398",
                    "plugin"),

        ("DisableStickerSuggestions",
                    "DisableStickerSuggestions.plugin.js",
                    "https://betterdiscord.app/Download?id=351",
                    "plugin"),

        ("MentionChannels",
                    "MentionChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=338",
                    "plugin"),

        ("PinIcon",
                    "PinIcon.plugin.js",
                    "https://betterdiscord.app/Download?id=421",
                    "plugin"),

        ("HideIconBadge",
                    "HideIconBadge.plugin.js",
                    "https://betterdiscord.app/Download?id=189",
                    "plugin"),

        ("HideEmbedLink",
                    "HideEmbedLink.plugin.js",
                    "https://betterdiscord.app/Download?id=171",
                    "plugin"),

        ("RedditMentions",
                    "RedditMentions.plugin.js",
                    "https://betterdiscord.app/Download?id=179",
                    "plugin"),

        ("HideMutedCategories",
                    "HideMutedCategories.plugin.js",
                    "https://betterdiscord.app/Download?id=82",
                    "plugin"),

        ("ClickableMentions",
                    "ClickableMentions.plugin.js",
                    "https://betterdiscord.app/Download?id=352",
                    "plugin"),

        ("TimedLightDarkMode",
                    "TimedLightDarkMode.plugin.js",
                    "https://betterdiscord.app/Download?id=108",
                    "plugin"),

        ("CustomQuoter",
                    "CustomQuoter.plugin.js",
                    "https://betterdiscord.app/Download?id=70",
                    "plugin"),

        ("ChatUserIDsRedux",
                    "ChatUserIDsRedux.plugin.js",
                    "https://betterdiscord.app/Download?id=14",
                    "plugin"),

        ("VoiceEvents",
                    "VoiceEvents.plugin.js",
                    "https://betterdiscord.app/Download?id=182",
                    "plugin"),

        ("TeX",
                    "TeX.plugin.js",
                    "https://betterdiscord.app/Download?id=379",
                    "plugin"),

        ("ChatAliases",
                    "ChatAliases.plugin.js",
                    "https://betterdiscord.app/Download?id=65",
                    "plugin"),

        ("HideMutedServers",
                    "HideMutedServers.plugin.js",
                    "https://betterdiscord.app/Download?id=194",
                    "plugin"),

        ("AvatarsEverywhere",
                    "AvatarsEverywhere.plugin.js",
                    "https://betterdiscord.app/Download?id=500",
                    "plugin"),

        ("HideUtils",
                    "HideUtils.plugin.js",
                    "https://betterdiscord.app/Download?id=17",
                    "plugin"),

        ("HideSideBar",
                    "HideSideBar.plugin.js",
                    "https://betterdiscord.app/Download?id=344",
                    "plugin"),

        ("UnreadCountBadges",
                    "UnreadCountBadges.plugin.js",
                    "https://betterdiscord.app/Download?id=395",
                    "plugin"),

        ("UserNotes",
                    "UserNotes.plugin.js",
                    "https://betterdiscord.app/Download?id=110",
                    "plugin"),

        ("Better Picture-In-Picture",
                    "Better-Picture-In-Picture.plugin.js",
                    "https://betterdiscord.app/Download?id=429",
                    "plugin"),

        ("ClickToChat",
                    "ClickToChat.plugin.js",
                    "https://betterdiscord.app/Download?id=382",
                    "plugin"),

        ("QuickToggler",
                    "QuickToggler.plugin.js",
                    "https://betterdiscord.app/Download?id=364",
                    "plugin"),

        ("ToggleYourStuff",
                    "ToggleYourStuff.plugin.js",
                    "https://betterdiscord.app/Download?id=30",
                    "plugin"),

        ("LinkChannels",
                    "LinkChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=157",
                    "plugin"),

        ("ServerThemes",
                    "ServerThemes.plugin.js",
                    "https://betterdiscord.app/Download?id=476",
                    "plugin"),

        ("Hastebin",
                    "Hastebin.plugin.js",
                    "https://betterdiscord.app/Download?id=337",
                    "plugin"),

        ("VoiceModeAnnounce",
                    "VoiceModeAnnounce.plugin.js",
                    "https://betterdiscord.app/Download?id=420",
                    "plugin"),

        ("SubtleDevicePrompt",
                    "SubtleDevicePrompt.plugin.js",
                    "https://betterdiscord.app/Download?id=234",
                    "plugin"),

        ("BetterBotTags",
                    "BetterBotTags.plugin.js",
                    "https://betterdiscord.app/Download?id=509",
                    "plugin"),

        ("RemoveNoRole",
                    "RemoveNoRole.plugin.js",
                    "https://betterdiscord.app/Download?id=368",
                    "plugin"),

        ("ServerConfig",
                    "ServerConfig.plugin.js",
                    "https://betterdiscord.app/Download?id=489",
                    "plugin"),

        ("CanaryLinks",
                    "CanaryLinks.plugin.js",
                    "https://betterdiscord.app/Download?id=126",
                    "plugin"),

        ("EmojiParty",
                    "EmojiParty.plugin.js",
                    "https://betterdiscord.app/Download?id=523",
                    "plugin"),

        ("UrbanDictionary",
                    "UrbanDictionary.plugin.js",
                    "https://betterdiscord.app/Download?id=520",
                    "plugin"),

        ("DoubleClickVoiceChannels",
                    "DoubleClickVoiceChannels.plugin.js",
                    "https://betterdiscord.app/Download?id=535",
                    "plugin"),

        ("RoleFilter",
                    "RoleFilter.plugin.js",
                    "https://betterdiscord.app/Download?id=525",
                    "plugin"),
    )

    yn = input(
        f"[?] Download and Install all plugins (189 or select them manually): ")
    print("[+] PLEASE DO NOT CLOSE THE PROGRAM. DOWNLOADING 180 PLUGINS")
    if yn.lower().startswith("y"):
        for dlname, file_name, dllink, dltype in all_stuff:
            ftemp = open(f"{file_name}", "w", encoding="utf-8").write(
                req.get(f"{dllink}").text)
            logfile.write(
                f"{datetime.now()}: Downloaded - {dlname} ({dltype})\n")

    else:
        for dlname, file_name, dllink, dltype in all_stuff:
            yn = input(f"[?] Download - show hidden channels({dltype}): ")
            if yn.lower().startswith("y"):
                ftemp = open(f"{file_name}", "w", encoding="utf-8").write(
                    req.get(f"{dllink}").text)
                logfile.write(
                    f"{datetime.now()}: Downloaded - {dlname} ({dltype})\n")
            else:
                print(f"[-] Skipping {dlname} ({dltype})")
                logfile.write(
                    f"{datetime.now()}: Not downloading {dlname} ({dltype})\n")

    print("[!] DO NOT CLOSE THE SCRIPT. Istalling plugins")
    os.system(
        f"mv *.plugin.js /home/{USERNAME}/.config/BetterDiscord/plugins/")
    logfile.write(
        f"{datetime.now()}: Installed all downloaded better discord plugins\n")
    print("[+] Installed all downloaded better discord plugins")


def install_program(package_name: str,
                    package_manager: str,
                    description: str,
                    logfile  # TextIOWrapper ?
                    ):
    yn = input(f"[?] Install - {package_name} ({description}):")
    if yn.lower().startswith("y"):
        os.system(f"{package_manager} -S {package_name}")
        logfile.write(
            f"{datetime.now()}: Installed {package_name} with {package_manager}\n")
    else:
        print(f"[-] Skipping {package_name}")
        logfile.write(f"{datetime.now()}: Not installing {package_name}\n")


clear()

LOG = ""
log = open(f"{os.getcwd()}/pc.log", "w+", encoding="utf-8")
log.write(f"{datetime.now()}: Log file created, all imports were successfull\n")

os.system("pacman -S base-devel wget curl yay git --noconfirm")
log.write(
    f"{datetime.now()}: Installed base-devel, wget, curl, yay, git with pacman\n")


clear()
print(r"""
 _   _ _   _ _ _ _   _
| | | | |_(_) (_) |_(_) ___  ___
| | | | __| | | | __| |/ _ \/ __|
| |_| | |_| | | | |_| |  __/\__ \
 \___/ \__|_|_|_|\__|_|\___||___/
""")

utility_packages = (
    (
        "yakuake",
        "pacman",
        "Drop down terminal"
    ),
    (
        "bpytop",
        "pacman",
        "system monitor tool"
    ),
    (
        "htop",
        "pacman",
        "system monitor tool"
    ),
    (
        "flameshot",
        "pacman",
        "screenshot utility"
    ),
    (
        "spectacle",
        "pacman"
        "screenshot utility"
    ),
    (
        "woeusb",
        "pacman",
        "OS flashing tool"
    ),
    (
        "etcher",
        "yay",
        "OS flashing tool"
    ),
)

for utility_package_name, utility_package_manager, utility_package_description in utility_packages:
    install_program(
        package_name=utility_package_name,
        package_manager=utility_package_manager,
        description=utility_package_description,
        logfile=log
    )

clear()
print(r"""
 __  __          _ _
|  \/  | ___  __| (_) __ _
| |\/| |/ _ \/ _` | |/ _` |
| |  | |  __/ (_| | | (_| |
|_|  |_|\___|\__,_|_|\__,_|
""")

media_packages = (
    (
        "gimp",
        "pacman",
        "photo editor"
    ),
    (
        "jellyfin-media-player",
        "yay",
        "Media Player for Jellyfin"
    ),
    (
        "kdenlive",
        "pacman",
        "video editor"
    ),
    (
        "okular",
        "pacman",
        "PDF viewer for KDE"
    ),
    (
        "audacious",
        "pacman",
        "music player"
    ),
    (
        "audacity",
        "pacman",
        "audio editor"
    ),
    (
        "vlc",
        "pacman",
        "media player"
    )
)


for development_package_name, development_package_manager, messaging_package_description in media_packages:
    install_program(
        package_name=development_package_name,
        package_manager=development_package_manager,
        description=messaging_package_description,
        logfile=log
    )

clear()
print(r"""
 __  __           _   _
|  \/  | ___  ___| |_(_)_ __   __ _
| |\/| |/ _ \/ _ \ __| | '_ \ / _` |
| |  | |  __/  __/ |_| | | | | (_| |
|_|  |_|\___|\___|\__|_|_| |_|\__, |
                              |___/
""")

meeting_packages = (
    (
        "zoom",
        "yay",
        "online meeting platform"
    ),
    (
        "teams",
        "yay",
        "online meeting platform"
    )
)

for development_package_name, development_package_manager, messaging_package_description in meeting_packages:
    install_program(
        package_name=development_package_name,
        package_manager=development_package_manager,
        description=messaging_package_description,
        logfile=log
    )

clear()
print(r"""
 __  __                           _
|  \/  | ___  ___ ___  __ _  __ _(_)_ __   __ _
| |\/| |/ _ \/ __/ __|/ _` |/ _` | | '_ \ / _` |
| |  | |  __/\__ \__ \ (_| | (_| | | | | | (_| |
|_|  |_|\___||___/___/\__,_|\__, |_|_| |_|\__, |
                            |___/         |___/
""")

messaging_packages = (
    (
        "telegram-desktop",
        "pacman",
        "messaging app"
    ),
    (
        "whatsapp-for-linux",
        "pacman",
        "messaging app"
    ),
    (
        "signal-desktop",
        "pacman",
        "messaging app"
    )
)


# discord (messaging app) seperate custom command because of better discord and plugins
yn = input("[?] Install - discord (messaging app): ")
if yn.lower().startswith("y"):
    os.system("pacman -S discord")
    log.write(f"{datetime.now()}: Installed discord with pacman\n")

    # better discord
    yn = input("[?] Install - better discord (for discord): ")
    if yn.lower().startswith("y"):
        os.system(
            "curl -O https://raw.githubusercontent.com/bb010g/betterdiscordctl/master/betterdiscordctl")
        os.system("chmod +x betterdiscordctl")
        os.system("sudo mv betterdiscordctl /usr/local/bin")
        log.write(
            f"{datetime.now()}: Installed better discord for discord manually\n")
        os.system("betterdiscordctl install")
        yn = input(
            "[?] Install - better discord plugins (betterdiscord): ")
        if yn.lower().startswith("y"):
            better_discord_plugins(logfile=log)
        else:
            print("[-] Skipping better better discord plugins")
            log.write(
                f"{datetime.now()}: Not installing better discord plugins\n")
    else:
        print("[-] Skipping better discord")
        log.write(f"{datetime.now()}: Not installing better discord\n")
else:
    print("[-] Skipping discord")
    log.write(f"{datetime.now()}: Not installing discord\n")

for development_package_name, development_package_manager, messaging_package_description in messaging_packages:
    install_program(
        package_name=development_package_name,
        package_manager=development_package_manager,
        description=messaging_package_description,
        logfile=log
    )


clear()
print(r"""
 ____                 _                                  _
|  _ \  _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_
| | | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ ` _ \ / _ \ '_ \| __|
| |_| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_
|____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                             |_|
""")

development_packages = (
    (
        "eclipse-java",
        "yay",
        "IDE for Java"
    ),
    (
        "visual-studio-code-bin",
        "yay",
        "IDE"
    ),
    (
        "vscodium",
        "yay",
        "IDE (Open Source VS-Code)"
    ),
    (
        "pycharm-community-edition",
        "yay",
        "IDE for Python"
    ),
    (
        "sublime-text-4",
        "yay",
        "Text Editor"
    ),
    (
        "github-desktop",
        "yay",
        "Code Management and Version Control System"
    ),
)


for development_package_name, development_package_manager, messaging_package_description in development_packages:
    install_program(
        package_name=development_package_name,
        package_manager=development_package_manager,
        description=messaging_package_description,
        logfile=log
    )

log.write(f"{datetime.now()}: Installer completed. Have a nice day!")
log.close()
print("[+] Installer Completed\nHave a nice day!")
