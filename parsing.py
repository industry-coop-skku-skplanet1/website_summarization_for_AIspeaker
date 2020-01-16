# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

class Tag_parser :
    def __init__(self):
        your_data = ''' <title>아주대학교병원에 오신 것을 환영합니다.
         - 원내 병원시설
    </title>
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

        </div>'''
        soup = BeautifulSoup(your_data, 'html.parser')
        self.html = your_data
        self.title = {}
        self.contents = {}
        self.recursiveChildren(soup)

    def recursiveChildren(self,x):
        for child in x.recursiveChildGenerator():
            name = getattr(child, "name", None)
            if name is not None:
                if 'h' in name or 'title' in name:
                    self.title[name] = child.get_text()
                elif 'p' in name:
                    self.contents[str(self.title.values())] = child.get_text()
            elif not child.isspace():  # leaf node, don't print spaces
                self.contents[str(self.title.values())] = child

    def h_tag_parser(self):
        pass


t = Tag_parser()

for title in t.contents :
    print('title is ', title ,"contents is ", t.contents[title] )
