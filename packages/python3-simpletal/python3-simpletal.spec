%global srcname SimpleTAL
%global pkgname simpletal

Name:		python3-%{pkgname}
Version:	5.2
Release:	9%{?dist}
Summary:	An XML based template processor for TAL, TALES and METAL specifications
License:	BSD
URL:		http://www.owlfish.com/software/simpleTAL/
Source0:	http://www.owlfish.com/software/simpleTAL/downloads/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-%{pkgname}}

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and
METAL specifications used in Zope to power HTML and XML templates.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install

# remove x-bits from example files
find examples -name '*.py' -exec chmod -x {} \;


%check
%{__python3} runtests.py || :


%files
%doc Changes.txt README.txt
%doc documentation/html
%doc examples
%license LICENSE.txt
%{python3_sitelib}/%{pkgname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.2-2
- Rebuild for Python 3.6

* Tue Aug  9 2016 Thomas Moschny <thomas.moschny@gmx.de> - 5.2-1
- New package.

