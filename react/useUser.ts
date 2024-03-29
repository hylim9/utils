import { useQuery } from "@tanstack/react-query";
import { getMe } from "../api";
import { IUser } from "../types";

export default function useUser() {
  const { isPending, data, isError } = useQuery<IUser>({
    queryKey: ["me"],
    queryFn: getMe,
    retry: false,
  });
  return {
    userLoading: isPending,
    user: data,
    isLoggedIn: !isError,
    logInTime: new Date(),
  };
}
