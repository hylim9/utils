import { Flex, Heading, ToastId, useToast } from "@chakra-ui/react";
import { useCountdown } from "./useCountdown";
import { useNavigate } from "react-router-dom";
import { useEffect, useRef } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { logOut } from "../api";

const CountDownTimer = ({ targetDate }: any) => {
  const [days, hours, minutes, seconds] = useCountdown(targetDate);
  const navigate = useNavigate();
  const toast = useToast();
  const toastId = useRef<ToastId>();
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: logOut,
    onMutate: () => {
      toastId.current = toast({
        title: "자동 로그아웃됩니다.",
        description: "세션 종료",
        status: "loading",
        // position: "bottom-right",
      }); // setTimeout 으로 시간 설정 가능
    },
    onSuccess: () => {
      if (toastId.current) {
        toast.update(toastId.current, {
          status: "success",
          title: "로그아웃 완료!",
        });
        queryClient.removeQueries({ queryKey: ["building"] }); // 로그아웃 시 캐시 삭제
        queryClient.removeQueries({ queryKey: ["me"] }); // 로그아웃 시 캐시 삭제
        navigate("/");
      }
    },
  });
  useEffect(() => {
    if (days + hours + minutes + seconds <= 0) {
      mutation.mutate();
    }
  }, [days, hours, minutes, seconds]);

  if (days + hours + minutes + seconds <= 0) {
    return (
      <Flex justifyContent={"center"} alignItems={"center"} mr={2}>
        <Heading size={"xs"}>세션만료</Heading>
      </Flex>
    );
  } else {
    return (
      <Flex justifyContent={"center"} alignItems={"center"} mr={2}>
        <Heading size={"xs"}>{minutes}:</Heading>
        <Heading size={"xs"}>{seconds.toString().padStart(2, "0")}</Heading>
      </Flex>
    );
  }
};

export default CountDownTimer;
