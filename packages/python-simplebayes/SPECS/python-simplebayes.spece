%global srcname simplebayes

Name:           python-%{srcname}
Version:        1.5.8
Release:        11%{?dist}
Summary:        A memory-based, optional-persistence naïve bayesian text classifier

License:        MIT
URL:            https://github.com/hickeroar/simplebayes
# PyPI tarballs do not include tests.
# 1.5.8 is also incorrectly tagged as 1.5.7
# https://github.com/hickeroar/simplebayes/issues/2
Source0:        https://github.com/hickeroar/simplebayes/archive/1.5.7/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A memory-based, optional-persistence naïve bayesian text classifier. This work \
is heavily inspired by the python "redisbayes" module and this was written to \
alleviate the network/time requirements when using the bayesian classifier to \
classify large sets of text, or when attempting to train with very large sets \
of sample data.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-1.5.7

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
nosetests-3


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.8-5
- Drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.8-1
- Initial package.
