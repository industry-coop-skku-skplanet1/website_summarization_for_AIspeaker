# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

class Tag_parser :
    def __init__(self):
        your_data = '''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ko" lang="ko">
<head>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>아주대학교병원에 오신 것을 환영합니다.
         - 원내 병원시설
    </title>
    <link rel="shortcut icon" type="image/x-icon" href="https://cdn.ajoumc.or.kr/Hospital/Images/Common/favicon.ico" />
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/Js/jquery-1.8.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/Js/jquery-ui.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/Js/common.js?version=20121221"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/Js/FormUtil.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/Js/swfobject.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Hospital/Js/Aju.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Hospital/Js/FakeSelect.js"></script>
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Hospital/Js/FakeScroll.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.ajoumc.or.kr/Hospital/Css/Default.css" />
    <link rel="stylesheet" type="text/css" href="https://cdn.ajoumc.or.kr/Common/colorbox/colorbox.css" />
    <script type="text/javascript" src="https://cdn.ajoumc.or.kr/Common/colorbox/jquery.colorbox.js"></script>
    <meta property="og:image" content="https://cdn.ajoumc.or.kr/Common/Image/facebook.jpg" />
    <link rel="image_src" href="https://cdn.ajoumc.or.kr/Common/Image/facebook.jpg" />
    <script type="text/javascript">
        WDomain = "http://hosp.ajoumc.or.kr";
        Cdndomain = "https://cdn.ajoumc.or.kr/Hospital";
        $(function () {
            aju.init();
        });
        $(document).ready(function () {
            $(".PointMenu").find("li").hover(
                function () {
                    $(this).find("img").attr("src", $(this).find("img").attr("src").replace("_Def", "_Over"));
                },
                function () {
                    $(this).find("img").attr("src", $(this).find("img").attr("src").replace("_Over", "_Def"));
                }
            );
            
            });
         
    </script>
    

    <script type="text/javascript">
        //<![CDATA[
        depth1 = ("3" == 0) ? null : "3" - 1;
        depth2 = ("5" == 0) ? null : "5" - 1;
        depth3 = ("1" == 0) ? null : "1" - 1;

        //]]>
    </script>
    <style type="text/css">
        #gnb7:hover
        {
            height:400px;
        }
    </style>
</head>
<body>
    <form name="aspnetForm" method="post" action="GuideInside.aspx" id="aspnetForm">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTA3NDczNzg3Mg9kFgJmD2QWBmYPFgIeBFRleHQFNzxtZXRhIGh0dHAtZXF1aXY9IlgtVUEtQ29tcGF0aWJsZSIgY29udGVudD0iSUU9ZWRnZSIgLz5kAgEPFgIfAAUWIC0g7JuQ64K0IOuzkeybkOyLnOyEpGQCAw9kFgwCAQ8PFgIeC05hdmlnYXRlVXJsBQUjbm9uZWRkAgQPDxYCHgdWaXNpYmxlZ2RkAgYPDxYCHwJnZGQCCA8WAh8ABR8mbmJzcDs+Jm5ic3A767OR7JuQ7J207Jqp7JWI64K0ZAIJDxYCHwAFICZuYnNwOz4mbmJzcDvrs5Hsm5Dsi5zshKQg7JWI64K0ZAIKDxYCHwAFICZuYnNwOz4mbmJzcDvsm5DrgrQg67OR7JuQ7Iuc7ISkZGRFPADicvONRVP/auSergnGF+Z3tg==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="05CF7234" />
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWCwK5nK2yDgLF561xAsSboYIKAt+jkaUOApTWqJ8PAu+S79wHAvOosboLAuCxyPoOAoOmu2YCmeSw9QoCwPTe8wg6suJtS9RY/NVQof15eMvlL7LJLw==" />
</div>
        <!-- header -->
        <div id="header">
            <div class="skip_access">
                <h1 class="hidden">아주대학교병원 내용 바로가기 링크</h1>
                <ul>
                    <li><a href="#contentsArea">본문 바로가기</a></li>
                    <li><a href="#gnbheader">주메뉴 바로가기</a></li>
                    <li><a href="#quick">배너 바로가기</a></li>
                </ul>
            </div>
            <div class="utilMenu">
                <div class="insideWrap">  
                    <ul class="clear"> 
                        <li class="LanguageBtn">
                            <a href="#none" class="open ">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilLanguageBtn.gif" alt="Language" title="언어선택" /></a>
                            <div class="language">
                                <a href="https://global.ajoumc.or.kr/Eng/Index.aspx" target="_blank" title="새창으로 연결">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/EnglishBtn.gif" alt="English" title="영어" /></a>
                                <a href="https://global.ajoumc.or.kr/Chn/Index.aspx" target="_blank" title="새창으로 연결">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/ChineseBtn.gif" alt="Chinese" title="중국어" /></a>
                                <a href="https://global.ajoumc.or.kr/Rus/Index.aspx" target="_blank" title="새창으로 연결">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/RussianBtn.gif" alt="Russian" title="러시아어" /></a>
                                <!--<a href="http://global.ajoumc.or.kr/Rus/Index.aspx" class="language" onclick="alert('준비중 입니다.');return false;"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/RussianBtn.gif" alt="Russian" /></a>-->
                                <a href="#none" class="close">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilCloseLangBtn.gif" alt="Close" title="언어선택닫기" /></a>
                            </div>
                        </li>
                        <li class="SearchBtn">
                            <label for="ctl00_tbxSearchWord" class="hidden">통합검색</label>
                            <input name="ctl00$tbxSearchWord" type="text" maxlength="20" id="ctl00_tbxSearchWord" class="InputDef" onkeypress="if(event.which || event.keyCode){if((event.which==13) || (event.keyCode ==13)){return fnTotalSearch();}}" style="width: 136px;" />
                            <a id="ctl00_hlkSearch" href="../#none"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilSearchBtn.gif" alt="검색" /></a>
                        </li>
                        <!--
                    <li id="ctl00_liLogin"><a href="http://hosp.ajoumc.or.kr/Member/Login.aspx?RT=/HospitalGuide/GuideInside.aspx"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilLoginBtn.gif" alt="로그인" /></a></li>                    
                    
                    -->
                        <li><a href="https://www.ajoumc.or.kr/Index.aspx" target="_blank" title="새창으로 연결">
                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilHospitalBtn.gif" alt="아주대학교의료원" /></a></li>
                        <!--<li><a href="http://info.ajoumc.or.kr/WI01/wi0111p_pw.asp" target="_blank" title="새창으로 연결"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/UtilMemberBoardBtn.gif" alt="교직원 게시판" /></a></li>-->
                    </ul>
                </div>
            </div>
            <div class="insideWrap" id="gnbheader">
                <p class="logo">
                    <a href="http://hosp.ajoumc.or.kr/Index.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Tmp/@logo.jpg" alt="아주대학교병원" /></a>
                </p>
            </div>
            <div class="GnbMenuWrap">
                <div class="GnbDepth GnbMenu1">
                    <a href="http://hosp.ajoumc.or.kr/MedicalInfo/TimeTable.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_MedicalInfo_Def.gif" alt="진료 안내" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 진료 안내 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_MedicalInfo.gif" alt="진료안내" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/TimeTable.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo0.png" alt="진료 시간표" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/TreatmentStep.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo1.png" alt="외래 진료" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/TreatmentStep.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo1_0.png" alt="진료절차" /></a>
                                                    </p>
                                                </li>
                                                
                                                <li style="height: 45px;">
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/OpenCard.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo1_2.png" alt="진료비 오픈카드" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/EmergencyMedical.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo2.png" alt="응급 진료" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/HospitalizationGuide.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3.png" alt="입원 진료" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/HospitalizationGuide.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3_0.png" alt="입원 안내" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/HospitalRoomGuide.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3_1.png" alt="병실생활 안내" /></a>
                                                    </p>
                                                </li>
                                                <li style="height: 45px;">
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/NursingCareService.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3_4.png" alt="간호간병 통합서비스" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/VisitionGuide.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3_2.png" alt="면회 안내" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/LeaveHospitalGuide.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo3_3.png" alt="퇴원 안내" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/InsuranceGuide.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo4.png" alt="건강 보험" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/InsuranceGuide.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo4_0.png" alt="보험 안내" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/NoinsuranceRetrieve.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo4_1.png" alt="비급여 진료비" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/HomeHealth.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo5.png" alt="가정 간호" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/HospiceService.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo7.png" alt="호스피스 완화의료" /> 
                                                </a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/MedicalInfo/Counselling.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo6.png" alt="사회 사업" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/Counselling.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo6_0.png" alt="상담 안내" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/MedicalInfo/ServiceFund.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo6_1.png" alt="사회사업 기금" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/MedicalInfo/TimeTable.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo_Pmenu0_Def.png" alt="진료 시간표 : 진료과별, 의료진별 진료 시간표" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/MedicalInfo/TreatmentStep.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/MedicalInfo_Pmenu1_Def.png" alt="외래 진료 : 입원부터 퇴원까지의 모든 정보" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu2">
                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Traffic.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_HospitalGuide_Def.gif" alt="병원이용안내" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 병원이용안내 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_HospitalGuide.gif" alt="병원 이용안내" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Traffic.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide0.png" alt="찾아오시는 길" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/ParkingInfo.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide1.png" alt="주차 안내" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/TelephoneInfo.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide2.png" alt="주요 전화번호" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/BuildingGuide.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide3.png" alt="층별 위치안내" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideInside.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide4.png" alt="병원시설 안내" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideInside.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide4_0.png" alt="원내 병원시설" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideOutside.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide4_1.png" alt="원외 편의시설" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/AjouGalleryRetrieve.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide4_2.png" alt="아주 갤러리" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteer.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide5.png" alt="자원봉사" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteer.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide5_0.png" alt="자원봉사활동" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteertrst.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide5_1.png" alt="자원봉사영역" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/VolunteerJoin.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide5_2.png" alt="참여 안내" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/HospitalGuide/NoticeRetrieve.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide5_3.png" alt="공지사항" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/Traffic.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide_Pmenu0_Def.png" alt="찾아오시는 길 : 교통 수단별 병원 방문 안내" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/BuildingGuide.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalGuide_Pmenu1_Def.png" alt="층별 위치안내 : 병원 이용을 더욱 쉽고 빠르게" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu3">
                    <a href="http://hosp.ajoumc.or.kr/Center/Index.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_Center_Def.gif" alt="진료과/의료진" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 진료과/의료진 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_Doctor.gif" alt="진료과/의료진" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/SearchDoctor.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor0.png" alt="아주대 의료진" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/CenterIndex.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor2.png" alt="전문센터" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/PartIndex.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor3.png" alt="진료과" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/CancerIndex.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor5.png" alt="암센터" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/DentalIndex.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor6.png" alt="치과병원" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Center/ClinicIndex.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Doctor4.png" alt="전문클리닉" /></a>
                                            </p>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/Center/SearchDoctor.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Center_Pmenu0_Def.png" alt="의료진 찾기 : 아주대학교병원의 우수한 의료진" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/Center/PartIndex.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Center_Pmenu1_Def.png" alt="진료과 찾기 : 진료과 | 전문 센터 | 전문 클리닉" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu4">
                    <a href="http://hosp.ajoumc.or.kr/Reservation/Reserve.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_Reservation_Def.gif" alt="예약/조회/발급" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 예약/조회/발급 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_Reservation.gif" alt="예약/조회/발급" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Reservation/Reserve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation0.png" alt="예약" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/Reserve.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation0_0.png" alt="진료예약 안내" /></a>
                                                    </p>
                                                </li>
                                                <div id="ctl00_pnlHttp">
	
                                                    <li>
                                                        <p>
                                                            <a href="http://hosp.ajoumc.or.kr/Reservation/Index.aspx" id="reserveWin" class="FnReservation">
                                                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation0_1.png" alt="인터넷 진료예약" /></a>
                                                        </p>
                                                    </li>
                                                
</div>
                                                
                                                <li>
                                                    <p>
                                                        <a href="http://ts.ajoumc.or.kr/CUR/AddNew.aspx?smpc=DM00030004&ssc=0003&ssgc=DM&mc=DM00030036" title="새창으로 연결" target="_blank">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation0_2.png" alt="인터넷 검진예약" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Reservation/TreatmentSearchRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1.png" alt="조회" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/TreatmentSearchRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1_0.png" alt="진료예약 조회" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://ts.ajoumc.or.kr/Result/Retrieve.aspx?smpc=DM00030004&ssc=0003&ssgc=DM&mc=DM00030064" target="_blank">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1_1.png" alt="검진결과 조회" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/CheckingSearchRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1_2.png" alt="검사예약 조회" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/MedicalRecordRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1_3.png" alt="수진이력 조회" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/HospitalizationRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation1_4.png" alt="입원 예정일" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Reservation/Certificate.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation2.png" alt="발급" /></a>
                                            </p>
                                            <ol>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/Certificate.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation2_0.png" alt="제증명/진단서" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/MedicalRecord.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation2_1.png" alt="진료기록 사본" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/MedicalImage.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation2_2.png" alt="의료영상사본" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                        <a href="http://hosp.ajoumc.or.kr/Reservation/PaymentCertificate.aspx">
                                                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation2_3.png" alt="납입증명서" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/Reservation/Index.aspx" id="A1" class="FnReservation">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation_Pmenu0_Def.png" alt="인터넷 진료예약 : 간편하게 이용하는 진료 예약" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/Reservation/TreatmentSearchRetrieve.aspx" onclick="return fnLoginPage(this, 0);">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Reservation_Pmenu1_Def.png" alt="진료예약 조회 : 고객님의 병원 진료 예약 내역" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu5">
                    <a href="http://hosp.ajoumc.or.kr/Customer/Faq.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_Customer_Def.gif" alt="고객 서비스" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 고객 서비스 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_Customer.gif" alt="고객 서비스" />
                                </div>
                                <div class="depth2" style="position:absolute;z-index:125;left:227px;top:0;width:180px;height:320px;overflow:hidden;background:#fff;">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/Faq.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer0.png" alt="자주하는 질문" /></a>
                                            </p>
                                        </li>
                                        <!--li><p><a href="http://hosp.ajoumc.or.kr/Customer/CounselHealthAddNew.aspx" onclick="return fnLoginPage(this, 0);"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer1.png" alt="건강 상담" /></a></p></li-->
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/CounselMedicineAddNew.aspx" onclick="return fnLoginPage(this, 0);">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer2.png" alt="복약 상담" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/PraiseRetrieve.aspx" onclick="return fnLoginPage(this, 0);" >
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer6.png" alt="칭찬합니다" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/OpinionAddNew.aspx" onclick="return fnLoginPage(this, 0);">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer3.png" alt="고객의 소리" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/BabyRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer4.png" alt="신생아 탄생축하" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/Customer/PaperDownload.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer5.png" alt="서식 다운로드" /></a>
                                            </p>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/Customer/Faq.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer_Pmenu0_Def.png" alt="자주하는 질문 : 병원 이용 방법, 질병 정보 확인" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/Customer/CounselMedicineAddNew.aspx" onclick="return fnLoginPage(this, 0);">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer_Pmenu1_Def.png" alt="복약 상담 : 바르고 안전하게 사용하는 약" /></a></li>
                                     <li><a href="http://hosp.ajoumc.or.kr/Customer/PraiseRetrieve.aspx"onclick="return fnLoginPage(this, 0);" >
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Customer_Pmenu2_Def.png" alt="칭찬합니다 : 아주대학교병원에 전하는 칭찬편지" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu6">
                    <a href="http://hosp.ajoumc.or.kr/HealthInfo/HealthRetrieve.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_HealthInfo_Def.gif" alt="건강정보" /></a>
                </div>
                <div class="GnbMenu">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 건강정보 -->
                            <div class="menu">
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_HealthInfo.gif" alt="건강정보" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HealthInfo/HealthRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo0.png" alt="건강 칼럼" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HealthInfo/ColumnRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo1.png" alt="건강 강좌/학술 행사" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HealthInfo/DiseaseRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo2.png" alt="질병 정보" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HealthInfo/ExamRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo3.png" alt="검사 정보" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HealthInfo/HighTechRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo4.png" alt="첨단 장비" /></a>
                                            </p>
                                        </li>
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/HealthInfo/HealthRetrieve.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo_Pmenu0_Def.png" alt="건강 칼럼 : 최근 유행하는 건강 관련 정보" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HealthInfo/DiseaseRetrieve.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HealthInfo_Pmenu1_Def.png" alt="질병 정보 : 질병을 바르게 알고 진료 받자" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="GnbDepth GnbMenu7">
                    <a href="http://hosp.ajoumc.or.kr/HospitalInfo/Greeting.aspx">
                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Gnb_HospitalInfo_Def.gif" alt="병원 소개" /></a>
                </div>
                <div class="GnbMenu" id="gnb7"  style ="overflow:auto;">
                    <div class="insideWrap">
                        <div class="GnbWrap">
                            <!-- 병원 소개 -->
                            <div class="menu" >
                                <div class="depth1">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/Title_HospitalInfo.gif" alt="병원안내" />
                                </div>
                                <div class="depth2">
                                    <ul>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/Greeting.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo0.png" alt="병원장 인사말" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/ChiefHistory.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo7.png" alt="역대병원장" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/OrganizationChart.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo1.png" alt="조직도" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/History01.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo2.png" alt="임상 성과" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/HospitalNewsRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo3.png" alt="병원 소식" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/PressRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo4.png" alt="언론 보도" /></a>
                                            </p>
                                        </li>
                                        <li>
                                            <p>
                                                        <a href="https://ajoumc.recruiter.co.kr">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo5.png" alt="채용" /></a>
                                            </p>
                                             <ol>
                                                <li>
                                                    <p>
                                                        <a href="https://ajoumc.recruiter.co.kr">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo5_0.png" alt="채용 공고" /></a>
                                                    </p>
                                                </li>
                                                <li>
                                                    <p>
                                                         <a href="http://hosp.ajoumc.or.kr/HospitalInfo/RecruitBenefit.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo5_1.png" alt="복지 제도" /></a>
                                                    </p>
                                                </li>
                                            </ol>
                                        </li>
                                        <li>
                                            <p>
                                                <a href="http://hosp.ajoumc.or.kr/HospitalInfo/BiddingRetrieve.aspx">
                                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo6.png" alt="입찰 공고" /></a>
                                            </p>
                                        </li>
                                        <!--학교법인대우학원재활요양병원-->
                                        
                                    </ul>
                                </div>
                                <ul class="PointMenu">
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalInfo/HospitalNewsRetrieve.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo_Pmenu0_Def.png" alt="병원 소식 : 한 눈에 보는 아주대학교병원 소식" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalInfo/PressRetrieve.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Gnb/HospitalInfo_Pmenu1_Def.png" alt="언론 보도 : 언론 속에 비친 다양한 병원 소식" /></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- //header -->

        <!-- contents -->
        <div id="section">
            <div class="contentWrap">
                <!-- lsubNavArea -->
                <div id="subNaviArea">
                    <div class="character">
                        <ul class="clear">
                            
                            <li class="li0"><a href="http://hosp.ajoumc.or.kr/Member/Login.aspx?RT=/HospitalGuide/GuideInside.aspx">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb_Login.gif" alt="로그인" /></a></li>
                            <li class="li1"><a href="http://hosp.ajoumc.or.kr/Join/JoinGate.aspx">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb_Join.gif" alt="회원가입" /></a></li>
                            
                            <li class="li2">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb_Txt.gif" alt="글자" />
                                <a href="#none" title="+" class="EditFont">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/plus.gif" alt="+" /></a>
                                <a href="#none" title="-" class="EditFont">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/minus.gif" alt="-" /></a>
                            </li>
                        </ul>
                        <!--                    
				    <button title="+">+</button>
				    <button title="-">-</button>
                    -->
                    </div>

                    <div id="subNavi">


                        

                        <p class="Title">
                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_Title.gif" alt="병원 이용안내" />
                        </p>
                        <ul class="Lnb Type2">
                            <li>
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Traffic.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_0_Def.gif" alt="찾아오시는 길" /></a>
                                </p>
                            </li>
                            <li>
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/ParkingInfo.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_1_Def.gif" alt="주차 안내" /></a>
                                </p>
                            </li>
                            <li>
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/TelephoneInfo.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_2_Def.gif" alt="주요 전화번호" /></a>
                                </p>
                            </li>
                            <li>
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/BuildingGuide.aspx">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_3_Def.gif" alt="층별 위치안내" /></a>
                                </p>
                            </li>
                            <li class="Submenu">
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideInside.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_4_Def.gif" alt="편의시설 안내" /></a>
                                </p>
                                <ol>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideInside.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_4_0_Def.gif" alt="원내 편의시설" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/GuideOutside.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_4_1_Def.gif" alt="원외 편의시설" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/AjouGalleryRetrieve.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_4_2_Def.gif" alt="아주 갤러리" /></a></li>
                                </ol>
                            </li>
                            <li class="Submenu">
                                <p>
                                    <a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteer.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_5_Def.gif" alt="자원봉사" /></a>
                                </p>
                                <ol>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteer.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_5_0_Def.gif" alt="자원봉사활동" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/Volunteertrst.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_5_1_Def.gif" alt="자원봉사영역" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/VolunteerJoin.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_5_2_Def.gif" alt="참여 안내" /></a></li>
                                    <li><a href="http://hosp.ajoumc.or.kr/HospitalGuide/NoticeRetrieve.aspx" class="OverAc">
                                        <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lnb/Lnb2_5_3_Def.gif" alt="공지사항" /></a></li>
                                </ol>
                            </li>
                        </ul>

                        
                    </div>

                    <div id="subQuick">
                        <div class="ContArea">
                            <ul>
                                <li><a href="http://hosp.ajoumc.or.kr/Center/Index.aspx" class="OverAc">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lquick/Quick0_Def.gif" alt="의료진 소개" /></a></li>
                                <li><a href="http://hosp.ajoumc.or.kr/MedicalInfo/TimeTable.aspx" class="OverAc">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lquick/Quick1_Def.gif" alt="진료 시간표" /></a></li>
                                <!--<li><a href="#none" class="OverAc"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lquick/Quick2_Def.gif" alt="온라인 발급" /></a></li>-->
                                <li><a href="http://hosp.ajoumc.or.kr/Ajoustory/Index.aspx" class="OverAc">
                                    <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lquick/Quick3_Def.gif" alt="아주스토리" /></a></li>
                            </ul>
                            <span class="deco">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Lquick/deco.png" alt="" /></span>
                        </div>
                    </div>
                </div>
                <!-- //lsubNavArea -->

                <!-- locationArea -->
                <div class="historyLocation">
                    홈&nbsp;>&nbsp;병원이용안내&nbsp;>&nbsp;병원시설 안내&nbsp;>&nbsp;원내 병원시설
                </div>
                <!-- // locationArea -->

                <!-- contentsArea -->
                
<div id="contentsArea" class="HospitalGuide">
    <h1><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/Title/Guide.png" alt="병원시설 안내" /></h1>

    <div class="h2Area">
        <h2><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsideTitle.gif" alt="원내 병원시설 이용안내" /></h2>
	    <p>아주대학교병원 내에서 이용하실 수 있는 고객 편의 서비스와 병원시설을 안내해 드립니다.</p>
    </div>

    <div class="TabStyA" id="Anchor">
	    <ul>
	    <li class="on"><a href="#none" title="현재 페이지"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside01on.gif" alt="편의서비스" /></a></li>
	    <li class=""><a href="./GuideInside2.aspx#Anchor" title="페이지 이동"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside02off.gif" alt="식당/커피전문점" /></a></li>
	    <li class=""><a href="./GuideInside3.aspx#Anchor" title="페이지 이동"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside03off.gif" alt="기타 편의시설" /></a></li>
	    <li class=""><a href="./GuideInside4.aspx#Anchor" title="페이지 이동"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside04off.gif" alt="봉사실" /></a></li>
	    <li class=""><a href="./GuideInside5.aspx#Anchor" title="페이지 이동"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside05off.gif" alt="종교실" /></a></li>
        <li class=""><a href="./GuideInside6.aspx#Anchor" title="페이지 이동"><img src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/tab/GuideInside06off.gif" alt="강당/회의실" /></a></li>
	    </ul>
    </div>

    <div class="ListStyWebzine">
		<ul>
			<li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto11.jpg"  alt="고객 안내센터" />
				<h3>고객 안내센터</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 1층, 웰빙센터 1층</li>
                    <li><span class="PointColor">주요업무</span> : 초진환자 진료접수 안내, 진료과 위치 및 진료절차 안내, 병원 이용 안내</li>
                    <li><span class="PointColor">연락처</span> : 031-219-5500(본관) / 031-219-7115(웰빙센터)</li>
                </ul>			
			</li>
			<li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto12.jpg"  alt="의료원 서비스센터" />
				<h3>우편물 수발실</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 지하 2층</li>
                    <li><span class="PointColor">운영시간</span> : 08:00 ~ 17:00</li>
                    <li><span class="PointColor">주요업무</span> : 국내 및 해외 우편물 발송, 팩스서비스</li>
                    <li><span class="PointColor">연락처</span> : 031-219-4803</li>
                </ul>			
			</li>
			<li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto13.jpg"  alt="휴대폰 무료 충전 서비스" />
				<h3>휴대폰 무료 충전 서비스</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 1층 로비 에스컬레이터 옆</li>
                    <li><span class="PointColor">이용요금</span> : 무료</li>
                </ul>			
			</li>
			<li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto14.jpg"  alt="휠체어/유모차 대여 서비스" />
				<h3>휠체어/유모차 대여 서비스</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 1층 고객 안내센터</li>
                    <li><span class="PointColor">연락처</span> : 031-219-5500</li>
                </ul>			
			</li>
			<li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto15.jpg"  alt="무인 빨래방" />
				<h3>무인 빨래방</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 지하 2층 </li>
                    <li><span class="PointColor">운영시간</span> : 06:00~24:00 </li>
                    <li><span class="PointColor">이용요금</span> : 세탁 1,000원 / 건조 1,000원 / 세제 500원</li>
                </ul>			
			</li>
            <li>
				<img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto16.jpg"  alt="수유실" />
				<h3>수유실</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">위치</span> : 본관 1층 정형외과 앞 / 웰빙센터 2층 소아청소년과 내 </li>
                    <li><span class="PointColor">운영시간</span> : 평일 08:00~17:00 </li>
                </ul>			
			</li>
            <li>
			    <img  class="photo" src="https://cdn.ajoumc.or.kr/Hospital/Images/HospitalGuide/GuideInsidePhoto17.jpg"  alt="수어통역서비스" />
				<h3>수어통역서비스</h3>
                <ul class="BulSty1">
                    <li><span class="PointColor">운영시간</span> : 평일 08:00~17:00 </li>
                    <li><span class="PointColor">연락처</span> : 의료수어통역사 010-6522-1791 / 070-7947-1791(See Talk 영상통화) </li>
                </ul>			
			</li>
		</ul>
    </div>

</div>

                <!-- //contentsArea -->

                <!-- quick -->
                <div id="quick">


                    <!--
                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Tmp/@quick.jpg" alt="quick menu" usemap="#quickmenu"  />
                <map name="quickmenu">
                    <area shape="rect" coords="" href="#none" alt="" />
                    <area shape="rect" coords="0,86,28,171" href="http://hosp.ajoumc.or.kr/Center/PartIndex.aspx" alt="진료과 찾기" />
                    <area shape="rect" coords="" href="#none" alt="" />
                </map>
                -->

                </div>
                <!-- //quick -->
            </div>
        </div>
        <!-- //contents -->

        <!-- footer -->
        <div id="footer">
            <div class="shopcutMenu">
                <div class="Footmenu">
                    <div class="Footmenus">
                        <ul class="viewMenus clear">
                            <li class="viewMenu"><a href="#none" title="레이어 팝업으로 이동">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/BtnTotalMenu.gif" alt="전체 메뉴 보기" /></a></li>
                            <li class="viewMenu"><a href="#none" title="레이어 팝업으로 이동">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/BtnRelationMenu.gif" alt="관련 사이트 보기" /></a></li>
                        </ul>

                        <ul class="centerUl clear">
                            <li><a href="http://hosp.ajoumc.or.kr/indexHEXC.aspx" target="_blank" title="새창으로 연결">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Btn_Health.gif" alt="건강증진센터" /></a></li>
                            <li><a href="https://ts.ajoumc.or.kr/Main/Main.aspx?ssc=0006&ssgc=DM" target="_blank" title="새창으로 연결">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Btn_funeral.gif" alt="장례식장" /></a></li>
                            <li><a href="https://ts.ajoumc.or.kr/Main/Main.aspx?ssc=0002&ssgc=DM" target="_blank" title="새창으로 연결">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Btn_RelationCenter.gif" alt="진료협력센터" /></a></li>
                            <li><a href="https://ts.ajoumc.or.kr/Main/Main.aspx?ssc=0004&ssgc=DM" target="_blank" title="새창으로 연결">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Btn_medical.gif" alt="의료원 발전기금" /></a></li>
                            <li class="none"><a href="http://hosp.ajoumc.or.kr/Ajoustory/Index.aspx">
                                <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Btn_Story.gif" alt="아주스토리" /></a></li>

                        </ul>

                        <div class="Customer">
                            <img src="https://cdn.ajoumc.or.kr/Hospital/Images/Common/Fmenu/Txtcustomer.gif" alt="전화예약 1688-6114" />
                        </div>
                    </div>
                </div>
            </div>

            
            
            <div class="footer">
                <a href="http://hosp.ajoumc.or.kr/Etc/Email.aspx" title="새창으로 연결" onclick="window.open(this.href,'email','toolbar=no,scrollbars=no,menubar=no,width=400,height=209');return false;" class="email">이메일주소 무단수집거부</a>
                <a href="http://hosp.ajoumc.or.kr/Etc/Agreement.aspx" class="service">이용약관</a>
                <a href="http://hosp.ajoumc.or.kr/Etc/Protect.aspx" class="privacy">개인정보취급방침</a>
                <a href="http://hosp.ajoumc.or.kr/Etc/Authority.aspx" class="authority">환자윤리강령</a>
                <p class="copyrights hidden">
                    (443-380) 경기도 수원시 영통구 월드컵로 164  l   대표전화 : 1688-6114   l   전화예약센터 : 031-219-5451<br />
                    COPYRIGHT© Ajou University Medical Center. All Rights Reserved
                </p>
                <ul class="bannerLink">
                    <li class="ban1"><a href="#none">보건복지부 연구중심병원</a></li>
                    <li class="ban2"><a href="#none">국제의료기관 평가 JCI 인증</a></li>
                    <li class="ban3"><a href="#none">보건복지부 의료기관인증</a></li>
                    <li class="ban4"><a href="#none">관상동맥우회술 1등급 병원</a></li>
                    <li class="ban5"><a href="#none">보건복지부 경기지역암센터</a></li>
                </ul>
            </div>
            
        </div>
        <!-- //footer -->


        <!-- Hidden Field / Control -->
        <table cellspacing="0" cellpadding="0" width="98%" border="0" style="display: none;">
            <tr>
                <td>
                    <input type="hidden" name="ctl00$hdnSearchWord" id="ctl00_hdnSearchWord" />
                    <a id="ctl00_btnTotalSearch" href="javascript:__doPostBack('ctl00$btnTotalSearch','')"></a>
                    <input type="hidden" name="ctl00$hdnReplyPage" id="ctl00_hdnReplyPage" value="1" />
                    <a id="ctl00_hdnReplyPaging" href="javascript:__doPostBack('ctl00$hdnReplyPaging','')"></a>
                    <input type="hidden" name="ctl00$hdnPage" id="ctl00_hdnPage" value="1" />
                    <a id="ctl00_lbtnPaging" href="javascript:__doPostBack('ctl00$lbtnPaging','')"></a>
                    <input type="hidden" name="ctl00$hdnICMenuName" id="ctl00_hdnICMenuName" />
                    <input type="hidden" name="ctl00$hdnICTitle" id="ctl00_hdnICTitle" />
                    <a id="ctl00_btnICAdd" href="javascript:__doPostBack('ctl00$btnICAdd','')"></a>
                </td>
            </tr>
        </table>
        <!-- Hidden Field / Control //-->

        <script language="javascript" type="text/javascript">

            // ================================================
            // 통합검색
            // ================================================
            function fnTotalSearch() {
                if ($("#ctl00_tbxSearchWord").css("display") == "inline-block" || $("#ctl00_tbxSearchWord").css("display") == "inline") {
                    if ($("#ctl00_tbxSearchWord").val() == "") {
                        alert("검색어를 입력해주세요")
                        return false;
                    }
                    else {
                        $("#ctl00_hdnSearchWord").val($("#ctl00_tbxSearchWord").val());
	                __doPostBack('ctl00$btnTotalSearch','');
	                return true;
	            }
            }
        }

        // ================================================
        // 로그인 체크후 페이지 이동
        // ================================================
        function fnLoginPage(obj, isblank) {
            if ("False" == "True") {
                if (isblank == 1) {
                    window.open(obj.href, "newPage", "", false);
                }
                else {
                    location.href = obj.href;
                }
            }
            else {
                if (confirm("로그인이 필요한 서비스입니다.\n\r로그인하시겠습니까?")) {
                    location.href = "http://hosp.ajoumc.or.kr/Member/Login.aspx?RC=" + obj.href;
            }
        }
        return false;
    }

    // ================================================
    // 페이징
    // ================================================
    function fnGoList(pg) {
        document.getElementById("ctl00_hdnPage").value = pg;
        __doPostBack('ctl00$lbtnPaging','');
    }

            // ================================================
            // 리플 페이징
            // ================================================
            function fnGoReplyList(pg) {
                document.getElementById("ctl00_hdnReplyPage").value = pg;
                __doPostBack('ctl00$hdnReplyPaging','');
            }

            // ================================================
            // 유효성검사
            // ================================================
            function goSubmit() {
                var frm = document.aspnetForm;
                var fu = new FormUtil(frm);
                if (!fu.success()) return false;
            }

            // ================================================
            // 주소복사
            // ================================================
            function fnURLCopy() {
                window.clipboardData.setData("Text", location.href);
                alert('주소복사가 완료되었습니다');
            }

            // ================================================
            // 관심 컨텐츠 등록
            // ================================================
            function fnInterestContentsAdd(icMenuName, icTitle) {

                if ("False" == "True") {
                    document.getElementById("ctl00_hdnICMenuName").value = icMenuName;
                    document.getElementById("ctl00_hdnICTitle").value = icTitle;
                    __doPostBack('ctl00$btnICAdd','');
                }
                else {
                    if (confirm("로그인이 필요한 서비스입니다.\n\r로그인하시겠습니까?")) {
                        location.href = "http://hosp.ajoumc.or.kr" + "/Member/Login.aspx?RC=" + location.href;
	            }
	            else {
	                return false;
	            }
            }
        }
        // ================================================
        // 삭제 확인 메세지
        // ================================================
        function fnIsDel(msg) {
            if (!confirm(msg + " 정말 삭제하시겠습니까?"))
                return false;
            else {
                return true;
            }
        }


        // ================================================
        // 우측퀵 진료과 바로 가기
        // ================================================
        function fnGoMedicalPart(obj) {
            if ($(obj).val() != "") {
                location.href = "http://hosp.ajoumc.or.kr/Center/MedicalIntroduce.aspx?mpc=" + $(obj).val();
            }
        }
        </script>

        <script>
            (function (i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date(); a = s.createElement(o),
      m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
            })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

            ga('create', 'UA-40236366-1', 'ajoumc.co.kr');
            ga('send', 'pageview');

        </script>

    

<script type="text/javascript">
//<![CDATA[
window.status = 'VIEWSTATE : ' + document.getElementById("__VIEWSTATE").value.length;//]]>
</script>
</form>
</body>
</html>
'''
        soup = BeautifulSoup(your_data, 'html.parser')
        self.html = your_data
        self.tags = []
        self.titles = {}
        self.contents = {}
        self.recursiveChildren(soup)

    def recursiveChildren(self,x):
        for child in x.recursiveChildGenerator():
            name = getattr(child, "name", None)
            if name is not None:
                self.tags.append(name)
            else:
                if child.isspace() or len(self.tags) == 0 : # lear node, don't print spaces
                    continue
                else:
                    if 'h' in self.tags[-1] or 'span' in self.tags[-1]:
                        self.titles[self.tags[-1]] = child
                    else:
                        self.contents[str(self.titles.values())] = child
                if len(self.tags):
                    self.tags.pop(-1)


    def h_tag_parser(self):
        pass


t = Tag_parser()

for title in t.contents :
    print('title is ', title ,"contents is ", t.contents[title] )
