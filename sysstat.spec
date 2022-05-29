#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysstat
Version  : 12.6.0
Release  : 67
URL      : https://github.com/sysstat/sysstat/archive/v12.6.0/sysstat-12.6.0.tar.gz
Source0  : https://github.com/sysstat/sysstat/archive/v12.6.0/sysstat-12.6.0.tar.gz
Summary  : SAR, SADF, MPSTAT, IOSTAT, TAPESTAT, PIDSTAT and CIFSIOSTAT for Linux
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: sysstat-bin = %{version}-%{release}
Requires: sysstat-data = %{version}-%{release}
Requires: sysstat-license = %{version}-%{release}
Requires: sysstat-locales = %{version}-%{release}
Requires: sysstat-man = %{version}-%{release}
Requires: sysstat-services = %{version}-%{release}
BuildRequires : intltool-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd
Patch1: 0001-Add-stateless-support.patch

%description
The sysstat package contains the sar, sadf, mpstat, iostat, tapestat,
pidstat, cifsiostat and sa tools for Linux.
The sar command collects and reports system activity information.
The information collected by sar can be saved in a file in a binary
format for future inspection. The statistics reported by sar concern
I/O transfer rates, paging activity, process-related activities,
interrupts, network activity, memory and swap space utilization, CPU
utilization, kernel activities and TTY statistics, among others. Both
UP and SMP machines are fully supported.
The sadf command may  be used to display data collected by sar in
various formats (CSV, XML, etc.) and to draw graphs (SVG).
The iostat command reports CPU utilization and I/O statistics for disks.
The tapestat command reports statistics for tapes connected to the system.
The mpstat command reports global and per-processor statistics.
The pidstat command reports statistics for Linux tasks (processes).
The cifsiostat command reports I/O statistics for CIFS filesystems.

%package bin
Summary: bin components for the sysstat package.
Group: Binaries
Requires: sysstat-data = %{version}-%{release}
Requires: sysstat-license = %{version}-%{release}
Requires: sysstat-services = %{version}-%{release}

%description bin
bin components for the sysstat package.


%package data
Summary: data components for the sysstat package.
Group: Data

%description data
data components for the sysstat package.


%package doc
Summary: doc components for the sysstat package.
Group: Documentation
Requires: sysstat-man = %{version}-%{release}

%description doc
doc components for the sysstat package.


%package license
Summary: license components for the sysstat package.
Group: Default

%description license
license components for the sysstat package.


%package locales
Summary: locales components for the sysstat package.
Group: Default

%description locales
locales components for the sysstat package.


%package man
Summary: man components for the sysstat package.
Group: Default

%description man
man components for the sysstat package.


%package services
Summary: services components for the sysstat package.
Group: Systemd services

%description services
services components for the sysstat package.


%prep
%setup -q -n sysstat-12.6.0
cd %{_builddir}/sysstat-12.6.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653849659
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --disable-sensors \
--enable-nls \
--disable-file-attr \
--disable-install-cron \
--disable-stripping \
conf_dir=/usr/share/defaults/sysstat \
conf_file=sysstat
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1653849659
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sysstat
cp %{_builddir}/sysstat-12.6.0/COPYING %{buildroot}/usr/share/package-licenses/sysstat/3127907a7623734f830e8c69ccee03b693bf993e
cp %{_builddir}/sysstat-12.6.0/contrib/irqstat/LICENSE %{buildroot}/usr/share/package-licenses/sysstat/eb93c122a87516d45e194a88122b874a019cf0f8
DESTDIR=%{buildroot} make install_all
%find_lang sysstat
## Remove excluded files
rm -f %{buildroot}*/etc/sysconfig/sysstat

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-sleep/sysstat.sleep
/usr/lib64/sa/sa1
/usr/lib64/sa/sa2
/usr/lib64/sa/sadc

%files bin
%defattr(-,root,root,-)
/usr/bin/cifsiostat
/usr/bin/iostat
/usr/bin/mpstat
/usr/bin/pidstat
/usr/bin/sadf
/usr/bin/sar
/usr/bin/tapestat

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sysstat/sysstat
/usr/share/defaults/sysstat/sysstat.ioconf

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/sysstat-12.6.0/CHANGES
/usr/share/doc/sysstat-12.6.0/COPYING
/usr/share/doc/sysstat-12.6.0/CREDITS
/usr/share/doc/sysstat-12.6.0/FAQ.md
/usr/share/doc/sysstat-12.6.0/README.md
/usr/share/doc/sysstat-12.6.0/sysstat-12.6.0.lsm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sysstat/3127907a7623734f830e8c69ccee03b693bf993e
/usr/share/package-licenses/sysstat/eb93c122a87516d45e194a88122b874a019cf0f8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cifsiostat.1.xz
/usr/share/man/man1/iostat.1.xz
/usr/share/man/man1/mpstat.1.xz
/usr/share/man/man1/pidstat.1.xz
/usr/share/man/man1/sadf.1.xz
/usr/share/man/man1/sar.1.xz
/usr/share/man/man1/tapestat.1.xz
/usr/share/man/man5/sysstat.5.xz
/usr/share/man/man8/sa1.8.xz
/usr/share/man/man8/sa2.8.xz
/usr/share/man/man8/sadc.8.xz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/sysstat-collect.service
/usr/lib/systemd/system/sysstat-collect.timer
/usr/lib/systemd/system/sysstat-summary.service
/usr/lib/systemd/system/sysstat-summary.timer
/usr/lib/systemd/system/sysstat.service

%files locales -f sysstat.lang
%defattr(-,root,root,-)

