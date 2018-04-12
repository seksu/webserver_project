# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
# from django.db.models import Q
from django.db.models import Sum, Count
from decimal import Decimal
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import list_route
from .models import Searching_Detail
from camera.models import Camera_Detail
from .serializers import SearchSerializer, SearchAdminSerializer, SearchResultSerializer
from account.permissions import IsUserAdmin
from subprocess import Popen, PIPE
from account.permissions import IsSuperAdmin
from datetime import datetime, timezone, timedelta
from django.core.cache import cache
import os
# Create your views here.

class DeleteSearchingDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Searching_Detail.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsSuperAdmin, ]
        return super(DeleteSearchingDetailViewSet, self).get_permissions()

    def list(self, request):
        from django.utils import timezone
        check = datetime.now()
        for obj in Searching_Detail.objects.all()[1013:]:
            if (check - obj.timestamp).days >= 7:
                print(obj.timestamp)
                if obj.fullbody_path:
                    try:
                        print('/home/pansek/workspace/'+obj.fullbody_path)
                        os.remove('/home/pansek/workspace/'+obj.fullbody_path)
                    except:
                        print('no such file fullbody')
                if obj.face_path:
                    try:
                        print('/home/pansek/workspace/'+obj.face_path)
                        os.remove('/home/pansek/workspace/'+obj.face_path)
                    except:
                        print('no such file face')
                if obj.video_path:
                    try:
                        print('/home/pansek/workspace/'+obj.video_path)
                        os.remove('/home/pansek/workspace/'+obj.video_path)
                    except:
                        print('no such file video')
            # if
            # obj.delete()

        # self.get_queryset().first().delete()

        response = "Empty for Search"
        return Response(response, status=status.HTTP_200_OK)


class NotificationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Searching_Detail.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsUserAdmin, ]
        return super(NotificationViewSet, self).get_permissions()

    def list(self, request):
        from django.core.cache import cache
        company = request.user.company.name
        cache.set('company',company,60*60*24)
        index = cache.get('index')
        before = index-1
        search = cache.get(str(index))
        if index and search and cache.get(str(before)).video_path and (search.video_path != cache.get(str(before)).video_path):
            serializer = SearchResultSerializer(search)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)


class SearchAdminViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Searching_Detail.objects.all()
    serializer_class = SearchAdminSerializer

    def get_permissions(self):
        self.permission_classes = [IsSuperAdmin, ]
        return super(SearchAdminViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            red_search = serializer.data['red']
            green_search = serializer.data['green']
            blue_search = serializer.data['blue']
            date_search = serializer.data['date']
            stage = serializer.data['stage']
            pos_left_top = serializer.data['pos_left_top']
            pos_right_bot = serializer.data['pos_right_bot']
            queryset = self.get_queryset()
            if red_search:
                queryset = queryset.filter(shirtcolor_r__range=[red_search[0], red_search[1]])
                queryset = queryset.filter(shirtcolor_g__range=[green_search[0], green_search[1]])
                queryset = queryset.filter(shirtcolor_b__range=[blue_search[0], blue_search[1]])
            if date_search:
                queryset = queryset.filter(timestamp__range=date_search)
            if pos_left_top and pos_right_bot:
                pos_left_top[0] = Decimal(pos_left_top[0])
                pos_left_top[1] = Decimal(pos_left_top[1])
                pos_right_bot[0] = Decimal(pos_right_bot[0])
                pos_right_bot[1] = Decimal(pos_right_bot[1])
                max_x = max([pos_left_top[0],pos_right_bot[0]])
                min_x = min([pos_left_top[0],pos_right_bot[0]])
                max_y = max([pos_left_top[1],pos_right_bot[1]])
                min_y = min([pos_left_top[1],pos_right_bot[1]])
                camera = Camera_Detail.objects.filter(latitude_t__range=[min_x, max_x])
                # camera = Camera_Detail.objects.filter(Q(latitude_t__gte=น้อย) & Q(latitude_t__lte=มาก))
                camera = camera.filter(longitude_t__range=[min_y, max_y])
            else:
                return Response("Select Area", status=status.HTTP_400_BAD_REQUEST)
            response = []
            for camera_token in camera:
                camera_re = queryset.filter(camera__token=camera_token.token)
                email_find = []
                email_data = camera_re.values('account__email').annotate(Count('account__email'))
                if email_data:
                    for email in email_data:
                        email_find.append(email['account__email'])

                video_data = camera_re.values('video_path').annotate(Count('video_path'))
                video_find = []
                video_show = []
                if video_data and stage:
                    for video in video_data:
                        video_find.append({ "video_name" : video['video_path'][14:],
                                            "video_real" : video['video_path'],
                                            "full_name" : [],
                                            "video_path" : "/ipcam/"+video['video_path'][14:22]+"/"+video['video_path'][22:24]+"00/"+video['video_path'][6:]})
                    tail = stage*2
                    video_show = video_find[tail-2:tail]
                    # count += 1
                    # print(str(count)+ ">>>>" + "video tee jer\n",video_find)
                tail = (stage+1)*2
                if video_find[tail-2:tail]:
                    next = "yes"
                else:
                    next = "no"

                full_name = []
                if video_show:
                    for video in video_show:
                        video_real = camera_re.filter(video_path=video['video_real'])
                        name = video_real.values('account__first_name','account__last_name','account__email').annotate(Count('account__first_name'))
                        for f_name in name:
                            full_name.append({ "first_name" : f_name['account__first_name'],
                                               "last_name" : f_name['account__last_name'],
                                               "face_path" : "/media/" + str(f_name['account__email']) + "/5.jpg"
                                             })

                        video.update({ "full_name" : [name for name in full_name if name['first_name'] and name['last_name']]})



                date_data = camera_re.values('timestamp').annotate(Count('timestamp'))
                date_find = []
                if date_data:
                    for date in date_data:
                        if str(date['timestamp'].date()) not in date_find:
                            date_find.append(str(date['timestamp'].date()))


                # print(camera_re.values('account__email').annotate(Count('account__email')))

                # print("wakkkk !!",camera_re.values('video_path').first())
                if camera_re.values('video_path').first():
                    response.append({ "token" : camera_token.token,
                                      "latitude" : camera_token.latitude,
                                      "longitude" : camera_token.longitude,
                                      "find_frame" : camera_re.count(),
                                      "camera_name" : camera_token.name,
                                      "find_video" : video_data.count(),
                                      "list_email" : [email for email in email_find if email],
                                      "list_video" : video_show,
                                      "list_date" : date_find,
                                      "next_page_video" : next
                                      # "search" : SearchResultSerializer(queryset.filter(camera__token=camera_token.token), many=True).data
                                      })
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class SearchViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Searching_Detail.objects.all()
    serializer_class = SearchSerializer

    def get_permissions(self):
        self.permission_classes = [IsUserAdmin, ]
        return super(SearchViewSet, self).get_permissions()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pic_search = serializer.data['pic_search']
            red_search = serializer.data['red']
            green_search = serializer.data['green']
            blue_search = serializer.data['blue']
            date_search = serializer.data['date']
            floor_search = serializer.data['floor']
            stage = serializer.data['stage']
            company_id = serializer.data['company']
            queryset = self.get_queryset()

            if pic_search:
                import base64
                company = request.user.company.name
                user_path = 'media/search_' + company
                path = os.path.join(settings.BASE_DIR, user_path)
                print(path)
                if not os.path.exists(path):
                    os.makedirs(path)
                image_data = serializer.data['pic_search']
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[1]
                print('search' + '.jpg')
                save_path = os.path.join(path, 'search' + '.jpg')
                data = base64.b64decode(imgstr)
                img_data = data
                with open(save_path, 'wb') as destination:
                    destination.write(img_data)
                print('>>>>>>>>>>>>' + save_path)

                temp = infer(save_path)
                print("temp eiei :", temp)
                lines = temp.split('\n')
                lineEnd = lines[len(lines)-2]
                words = lineEnd.split(' ')
                result_pic = None
                if(words[0] == "Predict"):
                    result_pic = words[1]
                    print("word[1] >>>>",result_pic)
                queryset = queryset.filter(account__email=result_pic)
            if red_search:
                queryset = queryset.filter(shirtcolor_r__range=[red_search[0], red_search[1]])
                queryset = queryset.filter(shirtcolor_g__range=[green_search[0], green_search[1]])
                queryset = queryset.filter(shirtcolor_b__range=[blue_search[0], blue_search[1]])
            if date_search:
                queryset = queryset.filter(timestamp__range=date_search)
            if request.user.role == 2:
                if floor_search:
                    camera = Camera_Detail.objects.filter(floor__in=floor_search, company=request.user.company.id)
                else:
                    camera = Camera_Detail.objects.filter(company=request.user.company.id)
            elif request.user.role == 1:
                if floor_search:
                    camera = Camera_Detail.objects.filter(floor__in=floor_search,company=company_id)
                else:
                    camera = Camera_Detail.objects.filter(company=company_id)



            # if floor_search:
            #     queryset = queryset.filter(camera__floor__range=floor_search)

            # for obj in queryset:
            #     if obj.camera.token not in response:
            #         response.update({obj.camera.token: [obj]})
            #     else:
            #         response[obj.camera.token].append(obj)
            #
            # for token in response.keys():
            #     response[token] = SearchResultSerializer(response[token], many=True).data
            #
            # response.update({'token': []})
            # for token in response.keys():
            #     response['token'].append(token)

            # count = 0
            response = []

            for camera_token in camera:
                camera_re = queryset.filter(camera__token=camera_token.token)
                email_data = camera_re.values('account__email').annotate(Count('account__email'))
                email_find = []
                if email_data:
                    for email in email_data:
                        email_find.append(email['account__email'])

                video_data = camera_re.values('video_path').annotate(Count('video_path'))
                video_find = []
                video_show = []
                if video_data and stage:
                    for video in video_data:
                        video_find.append({ "video_name" : video['video_path'][14:],
                                            "video_real" : video['video_path'],
                                            "full_name" : [],
                                            "video_path" : "/ipcam/"+video['video_path'][14:22]+"/"+video['video_path'][22:24]+"00/"+video['video_path'][6:]})
                    tail = stage*2
                    video_show = video_find[tail-2:tail]
                    # count += 1
                    # print(str(count)+ ">>>>" + "video tee jer\n",video_find)
                tail = (stage+1)*2
                if video_find[tail-2:tail]:
                    next = "yes"
                else:
                    next = "no"

                if video_show:
                    for video in video_show:
                        video_real = camera_re.filter(video_path=video['video_real'])
                        name = video_real.values('account__first_name','account__last_name','account__email').annotate(Count('account__first_name'))
                        full_name = []
                        for f_name in name:
                            full_name.append({ "first_name" : f_name['account__first_name'],
                                               "last_name" : f_name['account__last_name'],
                                               "face_path" : "/media/" + str(f_name['account__email']) + "/5.jpg"
                                             })

                        video.update({ "full_name" : [name for name in full_name if name['first_name'] and name['last_name']]})



                date_data = camera_re.values('timestamp').annotate(Count('timestamp'))
                date_find = []
                if date_data:
                    for date in date_data:
                        if str(date['timestamp'].date()) not in date_find:
                            date_find.append(str(date['timestamp'].date()))


                # print(camera_re.values('account__email').annotate(Count('account__email')))

                # print("wakkkk !!",camera_re.values('video_path').first())
                if camera_re.values('video_path').first():
                    response.append({ "token" : camera_token.token,
                                      "latitude" : camera_token.latitude,
                                      "longitude" : camera_token.longitude,
                                      "find_frame" : camera_re.count(),
                                      "camera_name" : camera_token.name,
                                      "find_video" : video_data.count(),
                                      "list_email" : [email for email in email_find if email],
                                      "list_video" : video_show,
                                      "list_date" : date_find,
                                      "next_page_video" : next
                                      # "search" : SearchResultSerializer(queryset.filter(camera__token=camera_token.token), many=True).data
                                      })

            # serializer = SearchResultSerializer(queryset, many=True)
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






def infer(save_path):
    proc = Popen(
        'python2 /home/pansek/openface/demos/classifier.py infer /home/pansek/openface/demos/lab509_features/classifier.pkl ' + save_path,
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print('res[1] >>>>',res[1])
    result = str(res[0], 'utf-8')
    print('result >>>> ', result)
    return result
