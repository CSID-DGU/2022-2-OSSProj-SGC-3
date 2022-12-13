import firebase_admin 
from firebase_admin import credentials, firestore
import pyautogui as pg

from register import db
from Defs import *

def item_buy(user,item):
  
  if coin_buy(user,item)!=0: # 현재 보유한 코인량이 구매하고자 하는 아이템의 가격보다 많은 경우
    db.collection("User").document(user).update({"item":firestore.ArrayUnion([item])}) # DB 구매아이템 리스트에 아이템 새로 추가
    print(pg.alert(text=Content.buy_msg.value, title=Content.buy_msgtitle.value))
  else: # 아닐경우, 구매 불가하다는 안내창 출력
    print(pg.alert(text=Content.cannotBuy_msg.value, title=Content.cannotBuy_msgtitle.value))

def item_buyList_get(user): # 사용자가 구매한 아이템 리스트 가져오기
  itemList=db.collection("User").document(user).get().to_dict()
  return itemList["item"]

def item_apply(user,item): # 구매한 아이템을 게임에 적용
  db.collection("User").document(user).update({"item_apply":item})


def item_apply_get(user): # 현재 적용중인 아이템 가져오기
  field=db.collection("User").document(user).get().to_dict()
  return field["item_apply"]

def coin_set(user,new_coin): # 코인 추가
  db.collection("User").document(user).update({"coin":firestore.Increment(new_coin)})

def coin_get(user): # 사용자가 현재 보유한 코인량 가져오기
  field=db.collection("User").document(user).get().to_dict()
  return field["coin"]

def coin_buy(user,item): # 사용자가 보유한 코인량이 사용자가 구매하고자 하는 아이템의 가격보다 많은지 체크  
  if coin_get(user)>=Item.bullets_price.value and item=="bullets":
    db.collection("User").document(user).update({"coin":firestore.Increment(-Item.bullets_price.value)})
  elif coin_get(user)>=Item.missile_price.value and item=="missile":
    db.collection("User").document(user).update({"coin":firestore.Increment(-Item.missile_price.value)})
  elif coin_get(user)>=Item.missile2_price.value and item=="missile2":
    db.collection("User").document(user).update({"coin":firestore.Increment(-Item.missile2_price.value)})
  elif coin_get(user)>=Item.dagger_price.value and item=="dagger":
    db.collection("User").document(user).update({"coin":firestore.Increment(-Item.dagger_price.value)})
  else: # 아닐경우 0을 리턴
    return 0 

def coin_give(user,friend,coin): # 친구에게 아이템 선물하기 함수
  coin=int(coin)
  db.collection("User").document(friend).update({"coin":firestore.Increment(coin)})
  coin_set(user,-coin) # 친구에게 코인을 선물하면, 선물한 만큼 자신의 코인이 줄어듦

def rank_set(user,new_coin): #랭킹 DB 저장
  field=db.collection("User").document(user).get().to_dict()
  current_rank=field["rank"]
  if new_coin>current_rank:
    db.collection("User").document(user).update({"rank":new_coin})

def rank_get(user): # 최고점 score 가져오기
  field=db.collection("User").document(user).get().to_dict()
  return field["rank"]

def rank(user,score): # 최근 점수와 비교하여 더 높은 점수를 랭킹에 저장
    current_rank = rank_get(user)
    if current_rank < score:
        rank_set(user,score)

def rankList_get(): # 사용자 전체 랭킹 score을 가져와서 순위를 매긴 후, rankList 반환
  users_ref = db.collection('User')
  docs = users_ref.stream()
  rank_list=[]
  for doc in docs: # 각 사용자의 랭킹 score 가져오기
    doc=doc.to_dict()
    rank_list.append([doc["email"],doc["rank"]])
  rank_list.sort(key=lambda x:-x[1])
  for i , rank in enumerate(rank_list): # 랭킹 score가 높은 순서대로 순위 매기기
    rank_list[i]=[i+1,rank[0],rank[1]]
  return rank_list


