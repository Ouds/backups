//
//  XmlResolve.h
//  iPoc
//
//  Created by mac os on 11-9-20.
//  Copyright 2011年 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface XmlResolve : NSObject {
    
}

@property (nonatomic, retain)NSString *objName;
@property BOOL *isList;
@property (nonatomic, retain) NSMutableString *currentResult;
@property (nonatomic, retain) NSMutableDictionary *map;
@property (nonatomic, retain) NSMutableArray *list;

-(NSMutableDictionary *)getObject:(NSString *)elName xmlData:(NSData *)xmlData;
-(NSMutableArray *)getList:(NSString *)elName xmlData:(NSData *)xmlData;

@end
