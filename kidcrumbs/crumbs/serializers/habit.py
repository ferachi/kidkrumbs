from rest_framework import serializers
from crumbs.models import Habit, HabitOption, HabitResponse




class HabitOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitOption
        fields = "__all__"

class HabitSerializer(serializers.ModelSerializer):
    options = HabitOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Habit
        fields = ["id", "title", "description", "school", "options", "created_by"]

class HabitResponseListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        habit_responses = [HabitResponse(**item) for item in validated_data]
        return HabitResponse.objects.bulk_create(habit_responses)

    def update(self, instances, validated_data):
        response_mapping = {str(response.id): response for response in instances}
        data_mapping = {item['id'] : item for item in validated_data}

        data = []
        for response_id, _response in data_mapping.items():
            response = response_mapping.get(response_id, None)
            if response is None:
                data.append(self.child.create(_response))
            else:
                data.append(self.child.update(response, _response))


        for response_id, _response in response_mapping.items():
            if response_id not in data_mapping:
                response.delete()

        return data
        


class HabitResponseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    class Meta:
        list_serializer_class = HabitResponseListSerializer
        model = HabitResponse
        fields = "__all__"
