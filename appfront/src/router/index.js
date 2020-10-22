import {createRouter, createWebHashHistory} from 'vue-router'
import Index from '../views/Index'
import Concept from '../views/Concept'
import Contact from '../views/Contact'
import Enterprise from '../views/Enterprise'
import News from '../views/News'
import Team from '../views/Team'
import Search from '../views/Search'
import Index_concept from "@/components/index/Index_concept";
import Team_partner from "@/components/team/Team_partner"
import Team_global from "@/components/team/Team_global";
import Team_manager_adviser from "@/components/team/Team_manager_adviser";
import Team_post_investment_operation from "@/components/team/Team_post_investment_operation";
import Team_manager from '../components/team/Team_manager'
import Team_adviser from "@/components/team/Team_adviser"
import Team_post_investment from "@/components/team/Team_post_investment";
import Team_legal from "@/components/team/Team_legal";
import Team_operation from "@/components/team/Team_operation";


const routes = [
    {
        path: '/',
        redirect: '/index',

    },
    {
        path: '/index',
        name: 'Index',
        component: Index,
    },
    {
        path: '/index_concept',
        name: 'Index_concept',
        component: Index_concept,
    },
    {
        path: '/concept',
        name: 'Concept',
        component: Concept,
    },
    {
        path: '/team',
        name: 'Team',
        component: Team,
        children: [
            {
                path: '',
                redirect: '/team/partner'
            },
            {
                path: 'partner',
                name: 'Team_partner',
                component: Team_partner,
            },
            {
                path: 'global',
                name: 'Team_global',
                component: Team_global,
            },
            {
                path: 'manager_adviser',
                name: 'Team_manager_adviser',
                component: Team_manager_adviser,
                children: [
                    {
                        path: '',
                        redirect: '/team/manager_adviser/manager'
                    },
                    {
                        path: 'manager',
                        name: 'Team_manager',
                        component: Team_manager,
                    },
                    {
                        path: 'adviser',
                        name: 'Team_adviser',
                        component: Team_adviser
                    }
                ]
            },
            {
                path: 'post_investment_operation',
                name: 'Team_post_investment_operation',
                component: Team_post_investment_operation,
                children: [
                    {
                        path: '',
                        redirect: '/team/post_investment_operation/post_investment',
                    },
                    {
                      path: 'post_investment',
                      name: 'Team_post_inevstment',
                      component: Team_post_investment,
                    },
                    {
                        path: 'legal',
                        name: 'Team_legal',
                        component: Team_legal,
                    },
                    {
                        path: 'operation',
                        name: 'Team_operation',
                        component: Team_operation,
                    }

                ]
            }
        ]

    },
    {
        path: '/enterprise',
        name: 'Enterprise',
        component: Enterprise,
    },
    {
        path: '/news',
        name: 'News',
        component: News,
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact,
    },
    {
        path: '/search',
        name: 'Search',
        component: Search,
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
    linkActiveClass: 'active',
})


export default router
