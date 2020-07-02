%global commit 76e9481c1a183048d0a1af0148d9f0cbd3556753
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global project email-reply-parser
%global owner zapier
%global date 20140523

%global with_tests 0
#Test is failing :(
#Reported to upstream
#See: https://github.com/zapier/email-reply-parser/issues/17

%global pypi_name email_reply_parser

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %{date}git%{shortcommit}%{?dist}.20
Summary:        Email reply parser library for Python 2

License:        MIT
URL:            https://github.com/zapier/email-reply-parser
Source0:        https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{commit}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3

%description
A port of GitHub's Email Reply Parser library. Email Reply Parser makes it easy
 to grab only the last reply to an on-going email thread.

%package -n python3-%{pypi_name}
Summary:        Email reply parser library for Python 3
Requires:       python3
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python3 port of GitHub's Email Reply Parser library. Email Reply Parser makes
 it easy to grab only the last reply to an on-going email thread.

%prep
%setup -q -n %{project}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if 0%{?with_tests}
%check

%{__python3} setup.py test
%endif # with_test

%files -n python3-%{pypi_name}
%{!?_licensedir:%global license %%doc}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-20140523git76e9481.20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-20140523git76e9481.18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-20140523git76e9481.17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-20140523git76e9481.14
- Subpackage python2-email_reply_parser has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-20140523git76e9481.12
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.0-20140523git76e9481.11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-20140523git76e9481.7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20140523git76e9481.6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20140523git76e9481.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20140523git76e9481.4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 William Moreno Reyes  <williamjmorenor at gmail.com> - 0.3.0-20140523git76e9481.3
- Update Python Macros
- Include subpackages for python 2 and 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-20140523git76e9481.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 0.3.0-20140523git76e9481
- Define %%license macro for EPEL < 7

* Sun Mar 22 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 0.3.0-20140523git76e9481.1
- Initial package.
