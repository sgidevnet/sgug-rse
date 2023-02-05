Name:          vhd2vl
Version:       2.5
Release:       9%{?dist}
Summary:       VHDL to Verilog translator

License:       GPLv2+
Url:           http://doolittle.icarus.com/~larry/vhd2vl/
Source0:       http://doolittle.icarus.com/~larry/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: flex bison flex-devel

%description
vhd2vl is a VHDL to Verilog translation program.
It targets the translation of synthetisable RTL.
While far from complete it supports a useful
subset of VHDL, sufficient for complex designs.


%prep
%autosetup

# rpmlint warning: W: wrong-file-end-of-line-encoding /usr/share/doc/vhd2vl-2.4/examples/gh_fifo_async16_sr.vhd
echo -n -e "... Fixing the end-of-line encodings of $f  \t"
sed -i.bak -e 's|\r||g' examples/gh_fifo_async16_sr.vhd
touch -r examples/gh_fifo_async16_sr.vhd.bak examples/gh_fifo_async16_sr.vhd
%{__rm} -f examples/gh_fifo_async16_sr.vhd.bak
echo "done"

%{__sed} -i "s|gcc \${STANDARD} \${WARNS} -O2 -g|gcc \${STANDARD} \${WARNS} %{optflags}|" src/makefile


%build
%make_build -C src


%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -pm 755 src/%{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%doc README.txt changes
%license GPLv2.txt
%doc examples translated_examples/


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 2.5-6
- added gcc as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.5-1
- Rebuilt for latest upstream release, patch removed (sent upstream)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Filipe Rosset <rosset.filipe@gmail.com> - 2.4-7
- Patched to fix FTBFS, added flex-devel as BR, spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.4-1
- New upstream release
- Fixed RHBZ#660820 - FTBFS vhd2vl-2.3-1.fc14

* Fri May 06 2011 Karsten Hopp <karsten@redhat.com> 2.3-2.1
- add buildrequirement flex-static

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 12 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.3-1
- New upstream release

* Sun Nov 29 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.2-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.0-3
- fix for bison 2.4-2.fc11

* Sun Dec 14 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.0-2
- enabled parallel build

* Sat Dec 06 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 2.0-1
- Initial package for fedora
