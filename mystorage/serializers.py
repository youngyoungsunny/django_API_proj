from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username') # 글 작성할때 자동으로 author를 지정하게 만든다
    
    class Meta:
        model = Essay
        fields = ('pk', 'author_name', 'title', 'body')


class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True) # 이미지를 업로드하고 결과값을 받을 때 확인작업을 url로 하겠다는 뜻

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')


class FilesSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'myfile', 'desc')