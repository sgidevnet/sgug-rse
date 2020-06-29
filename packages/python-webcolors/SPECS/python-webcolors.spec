%global srcname webcolors
%global srcdesc \
A library for working with color names and color value formats defined by the\
HTML and CSS specifications for use in documents on the Web.\
\
Support is included for the following formats (RGB colorspace only; conversion\
to/from HSL can be handled by the colorsys module in the Python standard\
library):\
* Specification-defined color names\
* Six-digit hexadecimal\
* Three-digit hexadecimal\
* Integer rgb() triplet\
* Percentage rgb() triplet

Name:           python-%{srcname}
Version:        1.11.1
Release:        2%{?dist}
Summary:        A library for working with HTML and CSS color names and value formats

License:        BSD
URL:            https://github.com/ubernostrum/webcolors
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}


%description %{srcdesc}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname} %{srcdesc}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build
make -C docs html


%install
%py3_install


%check
nosetests-%{python3_version}


%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11.1-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.11.1-1
- Bumped version to 1.11.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.10-1
- Bumped version to 1.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.9.1-1
- Bumped version to 1.9.1

* Sun Jun 02 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.9-1
- Bumped version to 1.9

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.7-9
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7-4
- Python 2 binary package renamed to python2-webcolors
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.7-2
- Python 3 detection for epel7

* Fri Feb 10 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.7-1
- Bumped version to 1.7
- Updated URL

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.5-1
- Bumped version to 1.5
- Upstream now ships tests and documentation

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Dec 09 2013 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.4-1
- Initial spec
