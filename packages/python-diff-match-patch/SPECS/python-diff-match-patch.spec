%global        srcname diff-match-patch
%global        desc The Diff Match and Patch libraries offer robust algorithms to perform the \
operations required for synchronizing plain text.

Name:          python-%{srcname}
Version:       20181111
Release:       3%{?dist}
Summary:       Algorithms for synchronzing plain text

License:       ASL 2.0
URL:           https://pypi.python.org/pypi/diff-match-patch/
Source0:       https://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools

%description
%{desc}

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%setup -n %{srcname}-%{version}

%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v


%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/diff_match_patch*


%changelog
* Wed Jun 24 2020 David King <amigadave@amigadave.com> - 20181111-3
- BuildRequire python3-setuptools explicitly

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20181111-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 20181111-1
- Update to 20181111
- Drop shebang removal steps (fixed upstream)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20121119-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20121119-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 David King <amigadave@amigadave.com> - 20121119-6
- Remove Python 2 subpackage (#1629492)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20121119-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20121119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Sep 27 2016 David King <amigadave@amigadave.com> - 20121119-1
- Initial Fedora packaging (#1379778)
