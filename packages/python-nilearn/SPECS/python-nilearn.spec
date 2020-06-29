%global srcname nilearn

%global desc %{expand: \
Nilearn is a Python module for fast and easy statistical learning on
NeuroImaging data.

It leverages the scikit-learn Python toolbox for multivariate statistics with
applications such as predictive modelling, classification, decoding, or
connectivity analysis.

This work is made available by a community of people, amongst which the INRIA
Parietal Project Team and the scikit-learn folks, in particular P. Gervais, A.
Abraham, V. Michel, A. Gramfort, G. Varoquaux, F. Pedregosa, B. Thirion, M.
Eickenberg, C. F. Gorgolewski, D. Bzdok, L. Esteve and B. Cipollini.

Detailed documentation is available at http://nilearn.github.io/.}

Name:           python-%{srcname}
Version:        0.6.2
Release:        3%{?dist}
Summary:        Python module for fast and easy statistical learning on NeuroImaging data

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist joblib}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist nibabel}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist setuptools}
Requires:  %{py3_dist numpy}
Requires:  %{py3_dist scipy}
Requires:  %{py3_dist scikit-learn}
Requires:  %{py3_dist joblib}
Requires:  %{py3_dist nibabel}
Recommends:  %{py3_dist matplotlib}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}
# Remove the addition of dummy sklearn requirement.
# Must be called before we remove lines and so on.
# Using line number so that if the file changes, this breaks the build instead
# of silently modifying something else.
sed -i '43 d' setup.py
# Remove shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;
# Remove pre-compiled files
find . -name "*pyc" -exec rm -f '{}' \;

%build
%py3_build

# Documentation also fetches imaging data set from online sources, so we cannot
# generate it. We include the link to the documentation in the description.

%install
%py3_install

%check
# Tests fetch data sets from online sources, and therefore cannot be run.

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.9

* Wed Apr 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.2-1
- Update to 0.6.2

* Thu Feb 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-2
- Remove dummy sklearn requirement from setup.py
- Remove py2 bits from spec

* Sun Feb 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-1
- Update to newest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sun Apr 14 2019 Manas Mangaonkar <pac23@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Wed Apr 10 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Ankur Sinha <ankursinha@fedoraproject.org> - 0.4.2-2
- Correct license
- Remvoe shebangs
- Remove pre-compiled files

* Thu Nov 08 2018 Ankur Sinha <ankursinha@fedoraproject.org> - 0.4.2-1
- Initial build
