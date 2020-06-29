%global srcname funcparserlib
%global srcdesc \
Parser combinators are just higher-order functions that take parsers as their\
arguments and return them as result values. Parser combinators are:\
* First-class values\
* Extremely composable\
* Tend to make the code quite compact\
* Resemble the readable notation of xBNF grammars\
\
Parsers made with funcparserlib are pure-Python LL(*) parsers. It means that\
it's very easy to write them without thinking about look-aheads and all that\
hardcore parsing stuff. But the recursive descent parsing is a rather slow\
method compared to LL(k) or LR(k) algorithms.\
\
So the primary domain for funcparserlib is parsing little languages or external\
DSLs (domain specific languages).

Name:           python-%{srcname}
Version:        0.3.6
Release:        24%{?dist}
Summary:        Recursive descent parsing library based on functional combinators

License:        MIT
URL:            https://github.com/vlasovskikh/funcparserlib
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist setuptools}


%description %{srcdesc}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname} %{srcdesc}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
nosetests-%{python3_version} build/


%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO README CHANGES
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%exclude %{python3_sitelib}/%{srcname}/tests


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-19
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.6-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.6-13
- Python 2 binary package renamed to python2-funcparserlib
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-11
- Python 3 detection for epel7

* Fri Feb 10 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-10
- Update URL

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.6-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Dec 21 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-2
- Using %%{python3_version} instead of hardcoded 3.3

* Mon Dec 09 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.3.6-1
- Initial spec
