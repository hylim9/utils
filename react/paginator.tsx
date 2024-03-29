import { Button, HStack } from "@chakra-ui/react";
import React, { useCallback, useEffect, useState } from "react";

export interface IPagePros {
  totalNum: number; // 전체 데이터 갯수
  itemPerPage: number; // 페이지 당 데이터 갯수
  pageShow: number; // 보여질 페이지 갯수
  //   page: number;
  //   setPage: (arg0: number) => void;
}
export default function Paginator({
  totalNum,
  itemPerPage,
  pageShow,
}: //   page,
//   setPage,
IPagePros) {
  const total = totalNum;
  const limit = itemPerPage;
  //   const numPages = Math.ceil(total / limit);
  //   const totalPages = new Array(numPages).fill(0); // 임의의 배열

  const totalPages = Math.ceil(total / limit);
  const [start, setStart] = useState<number>(1);
  const [page, setPage] = useState<number>(1);
  const pageNumShow = pageShow; // 5개씩 1-5 / 6-10
  const noPrev = start === 1;
  const noNext = start + pageNumShow - 1 >= totalPages;

  useEffect(() => {
    if (page === start + pageNumShow) setStart((prev) => prev + pageNumShow);
    if (page < start) setStart((prev) => prev - pageNumShow);
  }, [page, pageNumShow, start]);
  return {
    page: page,
    setPage: setPage,
    paginator: (
      <HStack
        //   h={"3vh"}
        w={"5%"}
        spacing={1}
        alignItems={"center"}
      >
        <Button
          size={"xs"}
          onClick={() => setPage(start - pageNumShow)}
          isDisabled={noPrev}
        >
          &lt;
        </Button>
        {[...Array(pageNumShow)].map((item, idx) => (
          <React.Fragment key={idx}>
            {start + idx <= totalPages && (
              <Button
                size={"xs"}
                key={start + 1}
                onClick={() => setPage(start + idx)}
              >
                {start + idx}
              </Button>
            )}
          </React.Fragment>
        ))}
        <Button
          size={"xs"}
          onClick={() => setPage(start + pageNumShow)}
          isDisabled={noNext}
        >
          &gt;
        </Button>
      </HStack>
    ),
  };
  // <HStack
  //   //   h={"3vh"}
  //   w={"5%"}
  //   spacing={1}
  //   alignItems={"center"}
  // >
  //   <Button
  //     size={"xs"}
  //     onClick={() => setPage(page - 1)}
  //     isDisabled={page === 1}
  //   >
  //     &lt;
  //   </Button>
  //   {totalPages.map((item, idx) => (
  //     <Button size={"xs"} key={idx + 1} onClick={() => setPage(idx + 1)}>
  //       {idx + 1}
  //     </Button>
  //   ))}
  //   <Button
  //     size={"xs"}
  //     onClick={() => setPage(page + 1)}
  //     isDisabled={page === numPages}
  //   >
  //     다음 &gt;
  //   </Button>
  // </HStack>
}
